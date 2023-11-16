from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class batting_model(BaseModel):
    Player : str
    Opponent_Country : str
    # def name(self):
    #     return self.Player
    # def country(self):
    #     return self.Country