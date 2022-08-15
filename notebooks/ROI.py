class ROI():
    def __init__(self, df, ytrue, ypred, threshold=0.8, name='XGBoost', seed=42):
        self.df = df.copy()
        self.df['true'] = ytrue
        self.df['pred'] = ypred
        self.df.sort_values('pred', ascending=False, inplace=True)
        self.threshold_ = threshold
        self.name_ = name
        self.seed_ = seed

    def make_LTV(self):
        self.mean_sal = self.df.salary.mean()
        self.df['LTV'] = round(self.df.salary.apply(lambda x: 0.15*x if x < self.mean_sal else 0.2*x), 2)

    def make_churn(self):
        self.df['churn'] = self.df.pred.apply(lambda x: 1 if x >= self.threshold_ else 0)
            
    def get_profit(self):
        profit = 0
        modelchurn = 0
        for i in range(self.ncards_):
            entry = self.df.iloc[i]
            if entry.true:
                profit += entry.LTV
                modelchurn += 1
        self.profit_ = profit - self.investment_
        self.model_churn_ = 100.*modelchurn / self.ncards_
            
    def get_random(self):
        randomdf = self.df.sample(self.ncards_, random_state=self.seed_)
        profit = 0
        randomchurn = 0
        for i in range(self.ncards_):
            entry = randomdf.iloc[i]
            if entry.true:
                profit += entry.LTV
                randomchurn += 1
        self.random_profit_ = profit - self.investment_
        self.random_churn_ = 100.*randomchurn / self.ncards_
        
    def greedy_knapsack(self):
        churndf = self.df.loc[self.df.churn == 1, :].copy()
        churndf.sort_values('LTV', ascending=False, inplace=True)
        greedy = 0
        greedychurn = 0
        i = 0
        n = min(len(churndf), self.ncards_)
        while i < n:
            entry = churndf.iloc[i]
            if entry.true:
                greedy += entry.LTV
                greedychurn += 1
            i += 1
        self.used_cards_ = i
        self.greedy_profit_ = greedy - (n * self.gift_)
        self.greedy_churn_ = 100.*greedychurn / n
        
    def make_gift(self):
        self.incentives_ = [20_000, 200, 100, 50]
        gifts = []
        n = len(self.df)
        for i in range(n):
            entry = self.df.iloc[i]
            if entry.pred >= .99:
                gifts.append(self.incentives_[0])
            elif entry.pred >= .95 and entry.pred < .99:
                gifts.append(self.incentives_[1])
            elif entry.pred >= .90 and entry.pred < .95:
                gifts.append(self.incentives_[2])
            else:
                gifts.append(self.incentives_[3])
        self.df['gift'] = gifts
        
    def random_gift(self):
        randomdf = self.df.sample(self.ncards_, random_state=self.seed_)
        profit = 0
        randomchurn = 0
        for i in range(self.ncards_):
            entry = randomdf.iloc[i]
            if entry.true:
                randomchurn += 1
                if entry.gift < self.incentives_[1] - 1:
                    profit += entry.LTV
        self.realrandom_profit_ = profit - self.investment_
        self.realrandom_churn_ = 100.*randomchurn / self.ncards_
        
    def give_gift(self):
        self.make_gift()
        self.random_gift()
        givedf = self.df[self.df.churn == 1]
        W = int(self.investment_ / self.incentives_[-1])
        vals = givedf.LTV.astype(int).values
        wt = (givedf.gift / self.incentives_[-1]).astype(int).values
        max_val, keep = knapsack(W, wt, vals)
        self.givedf = givedf[keep]
        profit = 0
        modelchurn = 0
        n = len(self.givedf)
        for i in range(n):
            entry = self.givedf.iloc[i]
            if entry.true:
                profit += (entry.LTV - entry.gift)
                modelchurn += 1
            else:
                profit += (0 - entry.gift)
        self.real_profit_ = profit
        self.real_churn_ = 100. * modelchurn / n

    def get_ROI(self):
        self.make_LTV()
        self.make_churn()
        self.get_profit()
        self.get_random()
        self.greedy_knapsack()
        self.give_gift()
        
    def print_performance(self, investment=10_000, gift=100, show=True):
        self.investment_ = investment
        self.gift_ = gift
        self.ncards_ = int(investment / gift)
        self.get_ROI()
        if show:
            print(f'Performance of {self.name_} - selecting the {self.ncards_} clients with highest churn probability:')
            print(f'ROI = ${self.profit_:,.2f}')
            print(f'Percentage of {self.ncards_} clientes that were correctly identified as churning clients: {self.model_churn_:.1f}%')

            print(f'\nPerformance of selecting the {self.used_cards_} richest clients (with Pchurn > {self.threshold_}):')
            print(f'ROI = ${self.greedy_profit_:,.2f}')
            print(f'Percentage of {self.used_cards_} clientes that were correctly identified as churning clients: {self.greedy_churn_:.1f}%')

            print(f'\nPerformance of randomly selecting {self.ncards_} clients:')
            print(f'ROI = ${self.random_profit_:,.2f}')
            print(f'Percentage of {self.ncards_} clientes that were correctly identified as churning clients: {self.random_churn_:.1f}%')

            print(f'\nPerformance of model in selecting clients (in realistic scenario):')
            print(f'ROI = ${self.real_profit_:,.2f}')
            print(f'Percentage of {len(self.givedf)} clientes that were correctly identified as churning clients: {self.real_churn_:.1f}%')
            print(f'Total invested: ${self.givedf.gift.sum():,}')
            
            print(f'\nPerformance of randomly selecting clients (in realistic scenario):')
            print(f'ROI = ${self.realrandom_profit_:,.2f}')
            print(f'Percentage of {self.ncards_} clientes that were correctly identified as churning clients: {self.realrandom_churn_:.1f}%')
        
    def get_results(self, investment=10_000, gift=100):
        self.print_performance(investment=investment, gift=gift, show=False)
        results = {}
        results['model']               = [self.name_]
        results                        = pd.DataFrame.from_dict(results)        
        results['threshold']           = self.threshold_
        results['total_ltv']           = self.df.LTV.sum()
        results['exiting_ltv']         = self.df.loc[self.df.true == 1, 'LTV'].sum()
        results['diff_ltv']            = results.total_ltv - results.exiting_ltv
        results['churn_ltv']           = self.df.loc[self.df.churn == 1, 'LTV'].sum()
        results['pred_ltv']            = results.total_ltv - results.churn_ltv
        results['churn_ratio']         = 100.*self.df.true.sum() / len(self.df.true)
        results['investment']          = self.investment_
        results['ncards']              = self.ncards_
        results['random_roi']          = self.random_profit_
        results['random_churn']        = self.random_churn_
        results['random_ltv']          = results.exiting_ltv - results.random_roi
        results['random_improve']      = results.random_roi / results.exiting_ltv
        results['random_ratio']        = results.random_churn / results.churn_ratio
        results['top100_prob_roi']     = self.profit_
        results['top100_prob_churn']   = self.model_churn_
        results['top100_prob_ltv']     = results.exiting_ltv - results.top100_prob_roi
        results['top100_prob_improve'] = results.top100_prob_roi / results.random_roi
        results['top100_prob_ratio']   = results.top100_prob_churn / results.random_churn
        results['top100_prob_eps']     = results.top100_prob_roi / results.exiting_ltv
        results['top100_prob_lift']    = results.top100_prob_churn / results.churn_ratio
        results['top100_rich_ncards']  = self.used_cards_
        results['top100_rich_roi']     = self.greedy_profit_
        results['top100_rich_churn']   = self.greedy_churn_
        results['top100_rich_ltv']     = results.exiting_ltv - results.top100_rich_roi
        results['top100_rich_improve'] = results.top100_rich_roi / results.random_roi
        results['top100_rich_ratio']   = results.top100_rich_churn / results.random_churn
        results['top100_rich_eps']     = results.top100_rich_roi / results.exiting_ltv
        results['top100_rich_lift']    = results.top100_rich_churn / results.churn_ratio
        results['real_random_roi']     = self.realrandom_profit_
        results['real_random_churn']   = self.realrandom_churn_
        results['real_random_ltv']     = results.exiting_ltv - results.real_random_roi
        results['real_random_improve'] = results.real_random_roi / results.exiting_ltv
        results['real_random_ratio']   = results.real_random_churn / results.churn_ratio
        results['real_ncards']         = len(self.givedf)
        results['real_roi']            = self.real_profit_
        results['real_churn']          = self.real_churn_
        results['real_ltv']            = results.exiting_ltv - results.real_roi
        results['real_improve']        = results.real_roi / results.real_random_roi
        results['real_ratio']          = results.real_churn / results.real_random_churn
        results['real_eps']            = results.real_roi / results.exiting_ltv
        results['real_lift']           = results.real_churn / results.churn_ratio
        return results