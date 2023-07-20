"""
Complexity Analysis
by leetcode Solution
Approach 2: Disjoint Set Union (DSU)
Here N is the number of accounts and K is the maximum length of an account.
Time complexity: O(NK⋅logNK+NK⋅α(N)).
Space complexity: O(NK)O(NK)O(NK)
"""


# ref = https://leetcode.com/problems/accounts-merge/solutions/109186/python-union-find-with-path-compression-and-building-disjoint-set-on-the-fly/
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py

        email_to_id = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_id[email].append(i)

        for ids in email_to_id.values():
            for _id in ids[1:]:
                union(ids[0], _id)

        merged_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            merged_accounts[find(i)].update(account[1:])

        return [[accounts[i][0]] + sorted(emails) for i, emails in merged_accounts.items()]
