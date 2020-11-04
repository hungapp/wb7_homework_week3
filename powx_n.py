class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2: #if n is odd then multiply with x 
            return x * self.myPow(x, n-1)
	# else square 
        return self.myPow(x*x, n/2)