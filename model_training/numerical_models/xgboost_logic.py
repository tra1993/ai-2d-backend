from xgboost import XGBRegressor
def create_xgboost(seed=42):
    return XGBRegressor(n_estimators=100, max_depth=5, random_state=seed)
