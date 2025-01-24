from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    username: str = Field(primary_key=True)
    email: str
    password: str
    created_at: Optional[datetime]

class PlayerHero(SQLModel, table=True):
    uuid: Optional[int] = Field(default=None, primary_key=True)
    map_type: str
    map_name: str
    player: str
    stat_name: str
    hero: str
    stat_amount: float
    match_date: datetime
    competition: str
    team: str
    match_id: int
    team_classification: int
    opponent: str
    opponent_classification: int

class PlayerMap(SQLModel, table=True):
    uuid: Optional[int] = Field(default=None, primary_key=True)
    start_time: datetime
    match_id: int
    competition: str
    map_type: str
    map_name: str
    player: str
    team: str
    stat_name: Optional[str]
    hero: str
    stat_amount: float

class Map(SQLModel, table=True):
    uuid: Optional[int] = Field(default=None, primary_key=True)
    round_start_time: datetime
    round_end_time: datetime
    competition: str
    match_id: int
    game_number: int
    match_winner: str
    map_winner: str
    map_loser: str
    map_name: str
    map_round: int
    winning_map_score: int
    losing_map_score: int
    control_round_name: str
    attacker: str
    defender: str
    team_one_name: str
    team_two_name: str
    attacker_payload_dist: Optional[float]
    defender_payload_dist: Optional[float]
    attacker_time_banked: Optional[float]
    defender_time_banked: Optional[float]
    attacker_control_percent: Optional[int]
    defender_control_percent: Optional[int]
    attacker_round_end_score: Optional[int]
    defender_round_end_score: Optional[int]

class Player(SQLModel, table=True):
    uuid: Optional[int] = Field(default=None, primary_key=True)
    player: str
    maps: int
    map_wins: int
    map_win_rate: float
    matches: int
    match_wins: int
    match_win_rate: float