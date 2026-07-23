class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Sort coins in descending order for the 'greedy' attempt
        coins.sort(reverse=True)
        
        # Initialize minimum coins found so far to infinity
        min_coins = float('inf')

        # This helper function will recursively explore combinations
        # current_index: index of the coin we are currently considering
        # current_amount: the remaining amount we need to make change for
        # count: the number of coins used so far for the current path
        def find_combinations(current_index, current_amount, count):
            nonlocal min_coins # Allows modifying min_coins from outer scope

            # Base case 1: If we made the exact amount, update min_coins
            if current_amount == 0:
                min_coins = min(min_coins, count)
                return

            # Base case 2: If we've gone through all coins or exceeded min_coins
            if current_index == len(coins) or count >= min_coins:
                return

            denom = coins[current_index]

            # The inner loop you suggested: try different multiples of the current denomination
            # We start from the maximum possible count for the current denomination
            # and go down to 0 (meaning we don't use this denomination at all for this path)
            for k in range(current_amount // denom, -1, -1):
                # If using 'k' coins of the current denomination,
                # the total count would exceed our best known solution,
                # then we can stop trying more of this denomination in this path.
                if count + k >= min_coins:
                    continue # Try fewer coins of this denom, or move to next denom

                remaining_amount = current_amount - k * denom
                
                # Recursively call with the next coin, the remaining amount, and updated count
                find_combinations(current_index + 1, remaining_amount, count + k)

        # Start the process from the first coin, with the full amount, and 0 coins used
        find_combinations(0, amount, 0)

        # If min_coins is still infinity, it means no solution was found
        return min_coins if min_coins!= float('inf') else -1
