class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occurence = {c: i for i, c in enumerate(S)}
        res = []
        partition_start = partition_end = 0
        for i, c in enumerate(S):
            partition_end = max(partition_end, last_occurence[c])
            if i == partition_end:
                res.append(partition_end - partition_start + 1)
                partition_start = partition_end + 1
        return res
