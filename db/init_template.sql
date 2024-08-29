USE master;
GO

IF DB_ID('$(MSSQL_DB)') IS NULL
BEGIN
    CREATE DATABASE $(MSSQL_DB);
    CREATE LOGIN $(MSSQL_LOGIN) WITH PASSWORD = '$(MSSQL_PASSWORD)';
END
GO

USE $(MSSQL_DB);
GO

IF NOT EXISTS (SELECT * FROM sys.database_principals WHERE name = '$(MSSQL_USER)')
BEGIN
    CREATE USER $(MSSQL_USER) FOR LOGIN $(MSSQL_LOGIN);
    EXEC sp_addrolemember 'db_datareader', '$(MSSQL_USER)';
END
GO

-- Create Users table if it doesn't exist
IF OBJECT_ID('dbo.Users', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Users (
        [Id] INT PRIMARY KEY IDENTITY(1,1),
        [Username] [varchar](200) NOT NULL,
        [Email] [varchar](200) NOT NULL,
        [Password] [varchar](200) NOT NULL,
        [Role] [varchar](50) NOT NULL,
        [CreatedAt] [datetime] DEFAULT GETDATE()
    );

    INSERT INTO dbo.Users (Username, Email, Password, Role) VALUES ('Admin', 'Admin@Admin.com', 'Admin123', 'Admin');
END
GO


--INSERT into hero data tables from csv files
IF OBJECT_ID('dbo.HeroData_2021', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.HeroData_2021;
END
GO

IF OBJECT_ID('dbo.HeroData_2022', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.HeroData_2022;
END
GO

IF OBJECT_ID('dbo.HeroData_2023', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.HeroData_2023;
END
GO

CREATE TABLE [dbo].[HeroData_2021](
    [MAP_TYPE] [varchar](200) NULL,
    [MAP_NAME] [varchar](200) NULL,
    [PLAYER] [varchar](200) NULL,
    [STAT_NAME] [varchar](200) NULL,
    [HERO] [varchar](200) NULL,
    [STAT_AMOUNT] [decimal](25, 8) NULL,
    [MATCH_DATE] [varchar](200) NULL,
    [COMPETITION] [varchar](200) NULL,
    [TEAM] [varchar](200) NULL,
    [MATCH_ID] [int] NULL,
    [TEAM_CLASSIFICATION] [int] NULL,
    [OPPONENT] [varchar](200) NULL,
    [OPPONENT_CLASSIFICATION] [int] NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[HeroData_2022](
    [MAP_TYPE] [varchar](200) NULL,
    [MAP_NAME] [varchar](200) NULL,
    [PLAYER] [varchar](200) NULL,
    [STAT_NAME] [varchar](200) NULL,
    [HERO] [varchar](200) NULL,
    [STAT_AMOUNT] [decimal](25, 8) NULL,
    [MATCH_DATE] [varchar](200) NULL,
    [COMPETITION] [varchar](200) NULL,
    [TEAM] [varchar](200) NULL,
    [MATCH_ID] [int] NULL,
    [TEAM_CLASSIFICATION] [int] NULL,
    [OPPONENT] [varchar](200) NULL,
    [OPPONENT_CLASSIFICATION] [int] NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[HeroData_2023](
    [MAP_TYPE] [varchar](200) NULL,
    [MAP_NAME] [varchar](200) NULL,
    [PLAYER] [varchar](200) NULL,
    [STAT_NAME] [varchar](200) NULL,
    [HERO] [varchar](200) NULL,
    [STAT_AMOUNT] [decimal](25, 8) NULL,
    [MATCH_DATE] [varchar](200) NULL,
    [COMPETITION] [varchar](200) NULL,
    [TEAM] [varchar](200) NULL,
    [MATCH_ID] [int] NULL,
    [TEAM_CLASSIFICATION] [int] NULL,
    [OPPONENT] [varchar](200) NULL,
    [OPPONENT_CLASSIFICATION] [int] NULL
) ON [PRIMARY]
GO

BULK INSERT dbo.HeroData_2021
FROM '/data/hero_data_2021.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.HeroData_2022
FROM '/data/hero_data_2022.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.HeroData_2023
FROM '/data/hero_data_2023.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

--INSERT into PHS tables from csv files
IF OBJECT_ID('dbo.PHS_2018', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.PHS_2018;
END
GO

IF OBJECT_ID('dbo.PHS_2019', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.PHS_2019;
END
GO

IF OBJECT_ID('dbo.PHS_2020', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.PHS_2020;
END
GO

IF OBJECT_ID('dbo.PHS_2021', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.PHS_2021;
END
GO

IF OBJECT_ID('dbo.PHS_2022', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.PHS_2022;
END
GO

IF OBJECT_ID('dbo.PHS_2023', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.PHS_2023;
END
GO

CREATE TABLE [dbo].[PHS_2018](
	[START_TIME] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[COMPETITION] [varchar](200) NULL,
	[MAP_TYPE] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[PLAYER] [varchar](200) NULL,
	[TEAM] [varchar](200) NULL,
	[STAT_NAME] [varchar](200) NULL,
	[HERO] [varchar](200) NULL,
	[STAT_AMOUNT] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[PHS_2019](
	[START_TIME] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[COMPETITION] [varchar](200) NULL,
	[MAP_TYPE] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[PLAYER] [varchar](200) NULL,
	[TEAM] [varchar](200) NULL,
	[STAT_NAME] [varchar](200) NULL,
	[HERO] [varchar](200) NULL,
	[STAT_AMOUNT] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[PHS_2020](
	[START_TIME] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[COMPETITION] [varchar](200) NULL,
	[MAP_TYPE] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[PLAYER] [varchar](200) NULL,
	[TEAM] [varchar](200) NULL,
	[STAT_NAME] [varchar](200) NULL,
	[HERO] [varchar](200) NULL,
	[STAT_AMOUNT] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[PHS_2021](
	[START_TIME] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[COMPETITION] [varchar](200) NULL,
	[MAP_TYPE] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[PLAYER] [varchar](200) NULL,
	[TEAM] [varchar](200) NULL,
	[STAT_NAME] [varchar](200) NULL,
	[HERO] [varchar](200) NULL,
	[STAT_AMOUNT] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[PHS_2022](
	[START_TIME] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[COMPETITION] [varchar](200) NULL,
	[MAP_TYPE] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[PLAYER] [varchar](200) NULL,
	[TEAM] [varchar](200) NULL,
	[STAT_NAME] [varchar](200) NULL,
	[HERO] [varchar](200) NULL,
	[STAT_AMOUNT] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[PHS_2023](
	[START_TIME] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[COMPETITION] [varchar](200) NULL,
	[MAP_TYPE] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[PLAYER] [varchar](200) NULL,
	[TEAM] [varchar](200) NULL,
	[STAT_NAME] [varchar](200) NULL,
	[HERO] [varchar](200) NULL,
	[STAT_AMOUNT] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

BULK INSERT dbo.PHS_2018
FROM '/data/phs_2018_stage_1.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2018
FROM '/data/phs_2018_stage_2.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2018
FROM '/data/phs_2018_stage_3.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2018
FROM '/data/phs_2018_stage_4.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2018
FROM '/data/phs_2018_playoffs.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2019
FROM '/data/phs_2019_stage_1.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2019
FROM '/data/phs_2019_stage_2.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2019
FROM '/data/phs_2019_stage_3.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2019
FROM '/data/phs_2019_stage_4.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2019
FROM '/data/phs_2019_playoffs.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2020
FROM '/data/phs_2020_1.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2020
FROM '/data/phs_2020_2.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2021
FROM '/data/phs_2021_1.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2021
FROM '/data/phs_2021_2.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2022
FROM '/data/phs_2022_1.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2022
FROM '/data/phs_2022_2.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.PHS_2023
FROM '/data/phs_2023.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

--INSERT into generic stat tables from csv files
IF OBJECT_ID('dbo.Match_Map_Stats', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.Match_Map_Stats;
END

IF OBJECT_ID('dbo.Player_Win_Rates', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.Player_Win_Rates;
END

CREATE TABLE [dbo].[Match_Map_Stats](
	[ROUND_START_TIME] [varchar](200) NULL,
	[ROUND_END_TIME] [varchar](200) NULL,
	[COMPETITION] [varchar](200) NULL,
	[MATCH_ID] [int] NULL,
	[GAME_NUMBER] [int] NULL,
	[MATCH_WINNER] [varchar](200) NULL,
	[MAP_WINNER] [varchar](200) NULL,
	[MAP_LOSER] [varchar](200) NULL,
	[MAP_NAME] [varchar](200) NULL,
	[MAP_ROUND] [int] NULL,
	[WINNING_MAP_SCORE] [int] NULL,
	[LOSING_MAP_SCORE] [int] NULL,
	[CONTROL_ROUND_NAME] [varchar](200) NULL,
	[ATTACKING_TEAM] [varchar](200) NULL,
	[DEFENDING_TEAM] [varchar](200) NULL,
	[TEAM_ONE_NAME] [varchar](200) NULL,
	[TEAM_TWO_NAME] [varchar](200) NULL,
	[ATTACKER_PAYLOAD_DIST] [decimal](25, 8) NULL,
	[DEFENDER_PAYLOAD_DIST] [decimal](25, 8) NULL,
	[ATTACKER_TIME_BANKED] [decimal](25, 8) NULL,
	[DEFENDER_TIME_BANKED] [decimal](25, 8) NULL,
	[ATTACKER_CONTROL_PERCENT] [int] NULL,
	[DEFENDER_CONTROL_PERCENT] [int] NULL,
	[ATTACKER_ROUND_END_SCORE] [int] NULL,
	[DEFENDER_ROUND_END_SCORE] [int] NULL
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Player_Win_Rates](
	[PLAYER] [varchar](200) NULL,
	[MAPS] [int] NULL,
	[MAP_WINS] [int] NULL,
    [MAP_WIN_RATE] [decimal](25, 8) NULL,
	[MATCHES] [int] NULL,
	[MATCH_WINS] [int] NULL,
	[MATCH_WIN_RATE] [decimal](25, 8) NULL
) ON [PRIMARY]
GO

BULK INSERT dbo.Match_Map_Stats
FROM '/data/match_map_stats.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO

BULK INSERT dbo.Player_Win_Rates
FROM '/data/player_win_rates.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
GO