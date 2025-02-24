# Task 1 
### Analyze the value each ad network brings to the overall business and provide recommendations. Our primary goal is to achieve a 35% blended ROAS D30. Explain your approach in detail and include calculations.

#
Below is a brief description of the analysis process and the relevant code snippets from [task1.py](/task1.py).

## Description

1. **Calculate CPA**  
    Iterate over each network’s spend and installs, computing both monthly and overall CPA (cost per acquisition). This helps determine cost efficiency of acquisition per network.

2. **Calculate ARPU**  
    ARPU (average revenue per user) is derived by attributing a proportion of the blended revenue based on each network’s fraction of installs.

3. **Simulate Different User Allocations**  
    Determine which combinations can achieve a target 35% ROAS while staying within the marketing budget of Month 4.

## Network Analysis

```
CPA PER MONTH
            Month1  Month2   Month3   Month4
NetworkA    $40.0   $42.86   $42.86   $50.00
NetworkB    $0.0    $0.00    $66.67   $66.67
NetworkC    $0.0    $0.00    $0.00    $33.33
```

```
REVENUE PER MONTH
            Month1       Month2      Month3      Month4
Organic    $14285.71   $16111.11   $18461.54    $6371.68
NetworkA   $35714.29   $38888.89   $43076.92   $23893.81
NetworkB       $0.00       $0.00   $18461.54   $11946.90
NetworkC       $0.00       $0.00       $0.00   $47787.61
```

```
OVERALL CPA PER NETWORK
Network    CPA
NetworkA   $44.00
NetworkB   $66.67
NetworkC   $33.33
```

```
OVERALL ARPU PER NETWORK
Network    ARPU  
Organic    $11.63
NetworkA   $11.33
NetworkB   $10.14
NetworkC   $7.96 
```

```
DISTRIBUTION OF INSTALLS PER NETWORK PER MONTH		
            Month1    Month2    Month3    Month4		
Organic	     29%	    29%	     23%	    7%
Network A	 71%	    71%	     54%	   27%
Network B	  0%	     0%	     23%	   13%
Network C	  0%	     0%	      0%	   53%

```
### Remarks

- As the marketing budget increases and activity on available networks grows, organic installs decline. This is expected, as potential organic users are more likely to be exposed to ads due to increased advertising efforts.
- We assume that the revenue generated per network is proportional to the total number of installs.
- Network B is the most expensive for acquiring new users and also has the lowest ARPU.
- Network C is more cost-effective for user acquisition but still has the lowest ARPU.
- To achieve maximum results, the budget should be optimally distributed across the three available channels.



## Simulation Approach
- **Target ROAS:** 35%  
- **Marketing Budget (Month 4):** $450,000
- **Bounds for Installs:** Determined by:

Lower bound for acquiring users from a certin network is set between 0 (i.e no users acquired from that network), while the upper bound is set as the max users that could be acquired based on the network with the lowest CPA. 

```python
lower_bound, upper_bound = 0, int(marketing_budget_month_4 / min(CPA.values()))
```

```python
def estimate_cpa(self) -> defaultdict:
     for network, marketing_budget in self.spend.items():
          # ...CPA calculations...

def estimate_revenue(self) -> defaultdict:
     for network, new_users in self.installs.items():
          # ...revenue attribution calculations...

def simulate_campaign_results(lower_bound, upper_bound, step, target_budget, target_revenue, ARPU, CPA):
     # ...simulation approach to find optimal budget allocation for Month 4...

# Main execution
NA = NetworkAnalysis(installs, spend, blended_revenue_d30)
CPA = NA.estimate_cpa()
ARPU = NA.estimate_revenue()

TARGET_PERCENTAGE = 0.35
marketing_budget_month_4 = sum(budget[-1] for budget in spend.values())
lower_bound, upper_bound = 0, int(marketing_budget_month_4 / min(CPA.values()))
target_revenue = marketing_budget_month_4 * TARGET_PERCENTAGE
step = 100

results = simulate_campaign_results(
     lower_bound=lower_bound,
     upper_bound=upper_bound,
     step=step,
     target_budget=marketing_budget_month_4,
     target_revenue=target_revenue,
     ARPU=ARPU,
     CPA=CPA
)
```
## Simulation Results
```
A blended 35% D30 ROAS cannot be achived!      
A blended 34% D30 ROAS cannot be achived!      
A blended 33% D30 ROAS cannot be achived!      
A blended 32% D30 ROAS cannot be achived!     
A blended 31% D30 ROAS cannot be achived!      
A blended 30% D30 ROAS cannot be achived!      
A blended 29% D30 ROAS cannot be achived!      
A blended 28% D30 ROAS cannot be achived!      

For achieving 27% blended ROAS D30 on Month 4 we allocate:
97.0% of the marketing budget to Network A     
0.0% of the marketing budget to Network B      
3.0% of the marketing budget to Network C  
```