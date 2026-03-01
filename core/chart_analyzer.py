class ChartAnalyzer:
    def __init__(self): self.last_index = 0
    def analyze_momentum(self, current_set):
        jump = current_set - self.last_index
        self.last_index = current_set
        status = "STABLE" if abs(jump) < 0.5 else "JUMPING"
        return {"momentum": status}
