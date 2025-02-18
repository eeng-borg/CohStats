from datetime import datetime
from os import name
from unittest import result
from games_list import GamesList
import pytest
import data
from enums import Factions


def _dummy_database_matches():
    return [
    {
        "id": 380940866,
        "creator_profile_id": 1428013,
        "mapname": "8p_general_mud",
        "maxplayers": 6,
        "matchtype_id": 3,
        "options": "eNozYPvGAAOMDGxAMrW0KL8glZGBiREktP1V6XbOk5eiYGrkGOVAJB4MAnxAbFEQn56al1qUmBOfW5rCMBgAANunDzs=",
        "slotinfo": "eNrNV9uSokgQ3W/xld6VO9gR+1DcFBURBBU39gER8YbYgEL3xP77CoU945jdsbExMTH1YiVSHDLz5MmEop/++tI6pcl6ewj14zr5Y7tqPTMCy4mC+NTKcj/fJkddaT3TT6089ONqSz611n5w+4N6aqV+EDZ/pP5xPwwv4eHdMvw82Divp/qO369359s4HIeplvpxaEzq+7aZHfqr1/phFeY5qy/HYe4rfu63nlsIIaldrUJFyEJ95LOcOrnur2tgB6hZ2m0jW92Taaub2uipq9t1ybrt9lLq7G0d24lW3K67t00fee1zWZK1wZQQRq/sbyKMMWLnEIZC6X5zYAFgSAjV/nzz++1SapfRx+vP1j9Pj/mjWFokKeYuf9TX/FF3+SO/5o/6ifmzBKZARu1EuCGh/O3mdrLFhgvGlrT4CB+Qcq7wHvO3mJCSndTGnMg0IH8ufSB9nD8RxBgsqF03qnMxBTnizFcXG7//pSi6gB95RkdrjOEaUvSIQdGDrFvbUgFi2Kupu8Vcp2CMHb3XsR9m4UN+vCaEiLmuuAryAB7+AN5xHYHjaeGOd+x/0A365/BOtjQuEKKGU4qAisc4TS5RjOMkEwzEKefC9ptcyKaoPOZC0wnZw5owbK+hfA8n77qz7DQ1cIexJLJho23HiwVh+I7TYBgpCfmRjEdlg+E6kfs9xgxF+mswWG47Gaf0XtjxWRgfdvt5x63qU/JktOsXp/OQftsbYRoRQkbMTHtN7a61W/HtMOxkGB9x5g33Hf/j85vqvBbpsnGUY/ayNK2SPyvC+Y3zOK091aXm3Zh1f9nm1c2o6ynzUOIPrM9FlZ8VPHg21Kx4Vi7ELsEEDFe0O+agJFzVp81R0rzXiHmdtYmN7tgxopgoPIXds2d47XlP0sx1UdC+10Xzt1e2ZDWDau+7xfe0/796LFKsyFN3dcH8Knp85fy8t5Yxs6IeAvTHGvBWo6PMOoP4GBdkMcKGB+qo5OxSqY6nYmgWgDGLEyLaYwPs572VarIYYzg/P3Cu0lFtbmE/EKzV7qlkClyQvAXpqJYv3lQTY2SgVjMDTcYYkg/GKtBI1WJxPwAxVDtbJWN8NQugWMlTaouDLIuAVvdReIq5CPecmV08xKqqL2d1MgyyvbAu3VF2IFl2YOZ0VduVrLiM7yijMe0Oy92yvzJNeZeu8heCf6GMRJltLMGJ7cQe6Pu25B5T1X4oBIS583EhwP1B5EiBo+/qgP/F5sq1MqU3OH+F5AI8VPPc8PA8aVhTkOudpd+LPpkrA6GdyTpWz9KDMFRXDEJsMDnEdVSwg95nc4mfl+2mT+0RyPXJm9rMJV0SrNmYiqymF9ogD13GmEhibXQ2CTTDvQRrFvcJXQTryclKvYd1gepGCOhTfekiZCPHsUcvArPIo4xeUON6xrGqRy0JQXFJ0vHPHXrpDUfxyqGv4842Ol06S+rEoLM+1uRAcjyNj+b9nvWDNJ2+DtgMyd9xmfvFZmz75a2wsKbyoKaqQSaqfczlAOTyIB1LMp4bj7Cmpqo+wVzmI1DvLtPbHN9VUojL6jsG+I107Q32kUIZ1h0CQVwe7S7NPPTBjL2YrV25eTZrAVye2kHSfOMFYKy03aJjDWtjLEQQBnu8pHiOV8YsVC+2pqSNHyzgx90aV4kUP6PllZd///YvirCK+A==",
        "description": "AUTOMATCH",
        "startgametime": 1734629945,
        "completiontime": 1734631489,
        "matchhistoryreportresults": [
            {
                "matchhistory_id": 380940866,
                "profile_id": 3745878,
                "resulttype": 1,
                "teamid": 0,
                "race_id": 0,
                "xpgained": 13336,
                "counters": "{\"abil\":31,\"blost\":0,\"bprod\":14,\"cabil\":3,\"cflags\":0,\"cpearn\":15,\"dmgdone\":12308,\"edeaths\":52,\"ekills\":111,\"erein\":36,\"fuelearn\":774,\"fuelmax\":334,\"fuelspnt\":460,\"gt\":1491,\"ismod\":0,\"manearn\":5750,\"manmax\":1298,\"manspnt\":4936,\"munearn\":1332,\"munmax\":510,\"munspnt\":850,\"pcap\":14,\"plost\":10,\"popmax\":0,\"precap\":9,\"sqkilled\":8,\"sqlost\":4,\"sqprod\":11,\"svetrank\":2,\"svetxp\":3480,\"upg\":12,\"utypes\":9,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":3,\"vp0\":460,\"vp1\":2,\"vprod\":3,\"vvetrank\":9,\"vvetxp\":5000,\"wpnpu\":0}",
                "matchstartdate": 1734629945
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 1428013,
                "resulttype": 0,
                "teamid": 1,
                "race_id": 1,
                "xpgained": 10604,
                "counters": "{\"abil\":14,\"blost\":1,\"bprod\":19,\"cabil\":3,\"cflags\":0,\"cpearn\":12,\"dmgdone\":5506,\"edeaths\":89,\"ekills\":33,\"erein\":43,\"fuelearn\":481,\"fuelmax\":338,\"fuelspnt\":380,\"gt\":1221,\"ismod\":0,\"manearn\":5348,\"manmax\":672,\"manspnt\":5065,\"munearn\":745,\"munmax\":380,\"munspnt\":365,\"pcap\":9,\"plost\":7,\"popmax\":0,\"precap\":12,\"sqkilled\":2,\"sqlost\":7,\"sqprod\":11,\"svetrank\":0,\"svetxp\":0,\"upg\":5,\"utypes\":5,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":0,\"vlost\":2,\"vp0\":460,\"vp1\":2,\"vprod\":3,\"vvetrank\":3,\"vvetxp\":1620,\"wpnpu\":1}",
                "matchstartdate": 1734629945
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 5975627,
                "resulttype": 1,
                "teamid": 0,
                "race_id": 2,
                "xpgained": 19659,
                "counters": "{\"abil\":78,\"blost\":4,\"bprod\":18,\"cabil\":2,\"cflags\":0,\"cpearn\":20,\"dmgdone\":18623,\"edeaths\":63,\"ekills\":129,\"erein\":50,\"fuelearn\":774,\"fuelmax\":264,\"fuelspnt\":755,\"gt\":1491,\"ismod\":0,\"manearn\":5706,\"manmax\":976,\"manspnt\":5779,\"munearn\":1332,\"munmax\":424,\"munspnt\":970,\"pcap\":13,\"plost\":7,\"popmax\":0,\"precap\":4,\"sqkilled\":18,\"sqlost\":5,\"sqprod\":13,\"svetrank\":4,\"svetxp\":4490,\"upg\":7,\"utypes\":11,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":10,\"vlost\":3,\"vp0\":460,\"vp1\":2,\"vprod\":7,\"vvetrank\":12,\"vvetxp\":7440,\"wpnpu\":9}",
                "matchstartdate": 1734629945
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 1814861,
                "resulttype": 0,
                "teamid": 1,
                "race_id": 1,
                "xpgained": 20853,
                "counters": "{\"abil\":44,\"blost\":0,\"bprod\":13,\"cabil\":9,\"cflags\":0,\"cpearn\":22,\"dmgdone\":24708,\"edeaths\":154,\"ekills\":46,\"erein\":79,\"fuelearn\":563,\"fuelmax\":356,\"fuelspnt\":350,\"gt\":1491,\"ismod\":0,\"manearn\":6097,\"manmax\":688,\"manspnt\":6447,\"munearn\":868,\"munmax\":214,\"munspnt\":830,\"pcap\":7,\"plost\":5,\"popmax\":0,\"precap\":6,\"sqkilled\":7,\"sqlost\":16,\"sqprod\":15,\"svetrank\":13,\"svetxp\":11860,\"upg\":5,\"utypes\":8,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":7,\"vlost\":8,\"vp0\":460,\"vp1\":2,\"vprod\":6,\"vvetrank\":5,\"vvetxp\":3220,\"wpnpu\":0}",
                "matchstartdate": 1734629945
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 5850752,
                "resulttype": 1,
                "teamid": 0,
                "race_id": 0,
                "xpgained": 12907,
                "counters": "{\"abil\":43,\"blost\":2,\"bprod\":14,\"cabil\":0,\"cflags\":0,\"cpearn\":15,\"dmgdone\":13275,\"edeaths\":92,\"ekills\":135,\"erein\":24,\"fuelearn\":774,\"fuelmax\":259,\"fuelspnt\":695,\"gt\":1491,\"ismod\":0,\"manearn\":5606,\"manmax\":839,\"manspnt\":5363,\"munearn\":1332,\"munmax\":312,\"munspnt\":1020,\"pcap\":15,\"plost\":12,\"popmax\":0,\"precap\":14,\"sqkilled\":13,\"sqlost\":4,\"sqprod\":14,\"svetrank\":0,\"svetxp\":0,\"upg\":14,\"utypes\":9,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":4,\"vlost\":1,\"vp0\":460,\"vp1\":2,\"vprod\":4,\"vvetrank\":11,\"vvetxp\":5480,\"wpnpu\":0}",
                "matchstartdate": 1734629945
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 2013306,
                "resulttype": 0,
                "teamid": 1,
                "race_id": 1,
                "xpgained": 11389,
                "counters": "{\"abil\":10,\"blost\":0,\"bprod\":14,\"cabil\":2,\"cflags\":0,\"cpearn\":12,\"dmgdone\":7049,\"edeaths\":93,\"ekills\":47,\"erein\":55,\"fuelearn\":479,\"fuelmax\":219,\"fuelspnt\":355,\"gt\":1215,\"ismod\":0,\"manearn\":5045,\"manmax\":622,\"manspnt\":4970,\"munearn\":742,\"munmax\":382,\"munspnt\":360,\"pcap\":13,\"plost\":10,\"popmax\":0,\"precap\":7,\"sqkilled\":2,\"sqlost\":8,\"sqprod\":11,\"svetrank\":2,\"svetxp\":1420,\"upg\":4,\"utypes\":6,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":0,\"vlost\":5,\"vp0\":460,\"vp1\":2,\"vprod\":5,\"vvetrank\":6,\"vvetxp\":3220,\"wpnpu\":1}",
                "matchstartdate": 1734629945
            }
        ],
        "matchhistorymember": [
            {
                "matchhistory_id": 380940866,
                "profile_id": 1428013,
                "race_id": 1,
                "statgroup_id": 6613825,
                "teamid": 1,
                "wins": 25,
                "losses": 28,
                "streak": -1,
                "arbitration": 2,
                "outcome": 0,
                "oldrating": 807,
                "newrating": 796,
                "reporttype": 3
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 5975627,
                "race_id": 2,
                "statgroup_id": 9935847,
                "teamid": 0,
                "wins": 1,
                "losses": 2,
                "streak": 1,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 952,
                "newrating": 986,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 5850752,
                "race_id": 0,
                "statgroup_id": 9935847,
                "teamid": 0,
                "wins": 1,
                "losses": 2,
                "streak": 1,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 952,
                "newrating": 986,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 3745878,
                "race_id": 0,
                "statgroup_id": 9935847,
                "teamid": 0,
                "wins": 1,
                "losses": 2,
                "streak": 1,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 952,
                "newrating": 986,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 1814861,
                "race_id": 1,
                "statgroup_id": 2246584,
                "teamid": 1,
                "wins": 1509,
                "losses": 1734,
                "streak": -1,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 952,
                "newrating": 941,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380940866,
                "profile_id": 2013306,
                "race_id": 1,
                "statgroup_id": 6613825,
                "teamid": 1,
                "wins": 25,
                "losses": 28,
                "streak": -1,
                "arbitration": 2,
                "outcome": 0,
                "oldrating": 807,
                "newrating": 796,
                "reporttype": 3
            }
        ]
    },
    {
        "id": 383842535,
        "creator_profile_id": 5975627,
        "mapname": "4p_coh2_okariver_frontline",
        "maxplayers": 8,
        "matchtype_id": 0,
        "options": "eNozYPvGgABsQJxaWpRfkMrIwMQI5DDa5dWtm/u4ORqmQo5RDkTiwSAgBcQmBfHJ+RlG8fnZiUWZZalF8WlF+XklOZl5qQwMmQw5QJjIkM6QyqDA4MhQDISJDKVAsRIGOgEAOKsY8w==",
        "slotinfo": "eNrNlluTokYUx/NZfNUJcsep2oduLiIjKCqjksoDchcBFUbQVL575GJ2XLFmN7Fmt1/opi+nT//O+XejWOePv1rbfez4G3sQOfHvvtV6Jkii2yO6nVaSGqkfRwOu9Ux2WqlthEX13OEY5qUD7bT2hmnXHXsjCob2wd7825KN1PRmx2054uk8OvVDe2zvhb0R2vK0HOcnE9uwjmW9sPmWlNXQTg3OSI3WcwsAHiJFyXgAVCABY69IuQuKQkIT1EW4VM5jIAABPDqC1C9/cLaQXTq1S0UC2oIaedU6aH67DqvyfBt1l2VjBBaX/1C91PjaVv2FSxYEfeQtQxWFx/YHK8TYkx5pvbiYVSwND3SizGYTZUfjeuommI6ODVV8eWFDBD3MI5MlXEaTMkFxFztoBhb4toyLg2DA/fLlS+vvzi1XnCZIhmauuGJfuaJXXLtfuRKfyNUy4yzvll7obbN/jyu6PYhiiY2T8BrPFddJPu17FaQkJfq3XEVKm8TVBIm2ofsB1+L7CAYo2u2SOH7FAL+XW+8YoJ/IwIZbf1r5O8uzu7mVHXtanVtbDjQwWKxZB1YNETbllrheU7xXNhTz/+QW/Om5RZE0RRPUFVfiO3IL/xyugjs4u46uxpg4V1UfSTPltObQTVz0n5iznoYeZAelh8PUZe8xDw2eH1S50u8B+Za5foTQr9ZJHZVrYM7G5w1UhmZdkH0H87XFbA5IPOW7uqtYhLhbePuQKzghAAxwR1oh5zBS+ktuYUNqQxikm697pslrJMJx+tZdQmc8XIuudlq01VVlh/O51wRZWjpkh20c4CN5PJ+v46OcOfIrqa6CQYZxL+TOIVnXRtt5ED8sVkiG7NIkdhUr1C+mAQ79inlE6YVV63FTPEzU5bTSYRalXe02HkwaSeq4IvNl0/3KcW5sVxqgNWhAAH04l2utZxt1ZuptXVjtlc7jBhuC/DpSq1yXY/lW6wPoMVptA+aN74RF7tv1eWRq1nifuECu/BgD48aPUrs0GGgbXAkiKrR3+ptmO6MTwdbaJQBdkKyTLrW30S5cbcTolLSPb4QqhtRx7FFu+2U0mOXDaQTmx1jNsMfFY48mKYy+ikf019GuMh5nOCH5fH2fM3ffBcNpMBlUZ75q1KdVOxnWd1t0aNKnM4cNU91Jgst/+C74UJ/4/6hPD+BanP47pE/oPY15eveIf3qoyqBXVH90l+hP2uWfv/0D55rZ0w==",
        "description": "SESSION_MATCH_KEY",
        "startgametime": 1738613003,
        "completiontime": 1738614684,
        "matchhistoryreportresults": [
            {
                "matchhistory_id": 383842535,
                "profile_id": 4540940,
                "resulttype": 0,
                "teamid": 0,
                "race_id": 0,
                "xpgained": 12577,
                "counters": "{\"abil\":11,\"blost\":2,\"bprod\":15,\"cabil\":2,\"cflags\":0,\"cpearn\":15,\"dmgdone\":12227,\"edeaths\":79,\"ekills\":66,\"erein\":31,\"fuelearn\":595,\"fuelmax\":156,\"fuelspnt\":535,\"gt\":1632,\"ismod\":0,\"manearn\":6809,\"manmax\":1016,\"manspnt\":6630,\"munearn\":980,\"munmax\":624,\"munspnt\":725,\"pcap\":7,\"plost\":5,\"popmax\":0,\"precap\":6,\"sqkilled\":4,\"sqlost\":11,\"sqprod\":16,\"svetrank\":1,\"svetxp\":1280,\"upg\":5,\"utypes\":8,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":4,\"vlost\":6,\"vp0\":0,\"vp1\":416,\"vprod\":4,\"vvetrank\":9,\"vvetxp\":4680,\"wpnpu\":0}",
                "matchstartdate": 1738613003
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 3745878,
                "resulttype": 1,
                "teamid": 1,
                "race_id": 4,
                "xpgained": 8213,
                "counters": "{\"abil\":62,\"blost\":3,\"bprod\":12,\"cabil\":2,\"cflags\":0,\"cpearn\":11,\"dmgdone\":12274,\"edeaths\":32,\"ekills\":79,\"erein\":34,\"fuelearn\":698,\"fuelmax\":207,\"fuelspnt\":605,\"gt\":1632,\"ismod\":0,\"manearn\":5878,\"manmax\":544,\"manspnt\":6005,\"munearn\":1117,\"munmax\":620,\"munspnt\":535,\"pcap\":4,\"plost\":2,\"popmax\":0,\"precap\":1,\"sqkilled\":3,\"sqlost\":2,\"sqprod\":10,\"svetrank\":2,\"svetxp\":1440,\"upg\":15,\"utypes\":11,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":1,\"vlost\":1,\"vp0\":0,\"vp1\":416,\"vprod\":2,\"vvetrank\":9,\"vvetxp\":5520,\"wpnpu\":2}",
                "matchstartdate": 1738613003
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 1100533,
                "resulttype": 0,
                "teamid": 0,
                "race_id": 1,
                "xpgained": 13129,
                "counters": "{\"abil\":50,\"blost\":0,\"bprod\":18,\"cabil\":3,\"cflags\":0,\"cpearn\":16,\"dmgdone\":17319,\"edeaths\":103,\"ekills\":80,\"erein\":60,\"fuelearn\":595,\"fuelmax\":177,\"fuelspnt\":550,\"gt\":1632,\"ismod\":0,\"manearn\":6225,\"manmax\":502,\"manspnt\":6305,\"munearn\":980,\"munmax\":407,\"munspnt\":585,\"pcap\":7,\"plost\":6,\"popmax\":0,\"precap\":4,\"sqkilled\":4,\"sqlost\":6,\"sqprod\":14,\"svetrank\":6,\"svetxp\":4190,\"upg\":6,\"utypes\":9,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":3,\"vp0\":0,\"vp1\":416,\"vprod\":7,\"vvetrank\":10,\"vvetxp\":5520,\"wpnpu\":0}",
                "matchstartdate": 1738613003
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 6576746,
                "resulttype": 1,
                "teamid": 1,
                "race_id": 3,
                "xpgained": 13637,
                "counters": "{\"abil\":6,\"blost\":1,\"bprod\":12,\"cabil\":1,\"cflags\":0,\"cpearn\":17,\"dmgdone\":19019,\"edeaths\":102,\"ekills\":75,\"erein\":63,\"fuelearn\":698,\"fuelmax\":404,\"fuelspnt\":365,\"gt\":1632,\"ismod\":0,\"manearn\":6112,\"manmax\":957,\"manspnt\":6161,\"munearn\":1117,\"munmax\":897,\"munspnt\":220,\"pcap\":11,\"plost\":5,\"popmax\":0,\"precap\":5,\"sqkilled\":9,\"sqlost\":11,\"sqprod\":17,\"svetrank\":2,\"svetxp\":2160,\"upg\":10,\"utypes\":13,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":6,\"vp0\":0,\"vp1\":416,\"vprod\":7,\"vvetrank\":14,\"vvetxp\":8820,\"wpnpu\":0}",
                "matchstartdate": 1738613003
            }
        ],
        "matchhistorymember": [
            {
                "matchhistory_id": 383842535,
                "profile_id": 5975627,
                "race_id": 3,
                "statgroup_id": 8865313,
                "teamid": 1,
                "wins": 32,
                "losses": 21,
                "streak": 2,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 1246,
                "newrating": 1261,
                "reporttype": 1
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 3745878,
                "race_id": 4,
                "statgroup_id": 5481760,
                "teamid": 1,
                "wins": 19,
                "losses": 15,
                "streak": 1,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 1038,
                "newrating": 1053,
                "reporttype": 1
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 6576746,
                "race_id": 3,
                "statgroup_id": 9949637,
                "teamid": 1,
                "wins": 4,
                "losses": 1,
                "streak": 2,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 1038,
                "newrating": 1077,
                "reporttype": 1
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 1100533,
                "race_id": 1,
                "statgroup_id": 1097756,
                "teamid": 0,
                "wins": 74,
                "losses": 52,
                "streak": -2,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 1267,
                "newrating": 1252,
                "reporttype": 1
            }
        ]
    },
    {
        "id": 384074602,
        "creator_profile_id": 5975627,
        "mapname": "6p_rzhev_frontline",
        "maxplayers": 6,
        "matchtype_id": 3,
        "options": "eNozYPvGAAOMDGxAMrW0KL8glZGBiREkdFlF+tJK3knRMDVyjHIgEg8GASEgNiuIL6rKSC2LTyvKzyvJycxLZRgMAAASzQ/V",
        "slotinfo": "eNrNl9tyqkgUhudZvNUZOTQCqdoXzRmDEVATcWouEDl7hgTjrnn3UZqYOK5M7ZqaSe2+sbth8dGrf//V0Ezn9++t7X4TpcvQXEeb39JF645GHMMwqNMqSr9MN2tTad0xnVYZ+qtzl+q0Ij94u0B3Wns/CJsLe3+dW+FLuLyMBn4ZJOPXbX3Hr6e7y3QV2uFe2/urcDCq70sLN/QXr/XDzsznop5ehaWv+KXfumthjKXuuVUqlh2Vi0xKxecm7wVc1T0sObhpuTTm9Eqp+wrWLvOTt04fj9AuwORClVzmtbeO7Oj6zKLIBTmfvs1/ZOwPbNYElLwzARi0JyUkgHYDgKGNAlYl63hwQAbHjJckQA4U7N0yPC1/cUnAHGTolht4JKCvDqT4lhExI5EEKIweA7lyzWVekSRnVaUDDHzJlT3xoXUkYTKUyCMQG9+s46qRfcafttafnVvNciLP9Rj+SrP0u2bpK81S75pFX6VZLXIFMyGJsSJoHwyFYw0yPwdy1MfjI+qnRC58iYB9UB/tdRDWAz1aQ4zumG4YcggyJq/GViaM4gFk5BeGZYW3jFOsg6XLr+TJOFsIy5fuZqRSs/hhgYzdNNmv6qjz/WzUn3d7avKge8o0lHpL5HPxIRODQJ1wXUWZbWNPimwrM+LJcdp25jeCsM9JFj4XDP72DdQM02NEkWGvNMP+gM8xX6GZXFqmL32SeElAFbRX5e7Q/Pf7dqEA/mII84oEaGsW8kljJg8VMn9gsAl4mO5kMcntoIzlW4Yh7gYq8S5pT0GM4TtDF/HglvFEM7vGJ/Wuc7OOk45Oa132X5u1ahTSAA9aTsycPNQ6xp/rMpdGl/dRMoT/By9iecQJvHClK/QDXkR/jRfV+XSkkd7knDuAdeM4dFXiV/IArE2lkrsmGedaBdSNSF3pjZewCciw+SJYkPongAyFNv0mYAYwpL/5zalW0Zd1oTa+8a//xDdEmu1duwb387hGaN3bJnF4DLrG3Ne6TRW5f4Fcw+jGUUV23uLBSpXaJt0MjqBreKL5lJL5pygAGLpfKuQtsf1ovz37IwOJxzFRl5yKMeAa0XZ1TIRPXePkfpkteo1jHYYQYyNkrkFUVSIHyFXI00xV1IP2M4aqob2h8pQM+ATKFW9P5zJxG4TAE9yjWhzIOqyhCjCMtbgorHowtAFn+9iUWgb/JGn49CRwFM8xV5ru/WSOFbWPh4QiopOgE7s6LgcecZNhALvJYu43JyzYsSYTXU0QEUQIVRlj2OVx2jCeIAau0D1hKI8gw4sfM4kwqhg6Tasb38PkhDUUwNP0WBvnRj1W7uGvgkhTGkYAf3kI3npDGAP4q6C9wUqzjgr4KnjC8elwMtP6i+Os396ud6v50lgfizaOz9uFJdfR3dE0YEbRbtbbrjj3VBLtYv+sStxzkaFwY6dZqgojaltpxU4dPMT/Rst//PIXaws6Fw==",
        "description": "AUTOMATCH",
        "startgametime": 1738951595,
        "completiontime": 1738953934,
        "matchhistoryreportresults": [
            {
                "matchhistory_id": 384074602,
                "profile_id": 1452224,
                "resulttype": 0,
                "teamid": 0,
                "race_id": 0,
                "xpgained": 21124,
                "counters": "{\"abil\":142,\"blost\":0,\"bprod\":15,\"cabil\":0,\"cflags\":0,\"cpearn\":24,\"dmgdone\":23032,\"edeaths\":131,\"ekills\":94,\"erein\":91,\"fuelearn\":872,\"fuelmax\":270,\"fuelspnt\":705,\"gt\":2272,\"ismod\":0,\"manearn\":8364,\"manmax\":872,\"manspnt\":8292,\"munearn\":1320,\"munmax\":172,\"munspnt\":1300,\"pcap\":11,\"plost\":10,\"popmax\":0,\"precap\":8,\"sqkilled\":9,\"sqlost\":10,\"sqprod\":17,\"svetrank\":3,\"svetxp\":3060,\"upg\":13,\"utypes\":8,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":3,\"vp0\":0,\"vp1\":451,\"vprod\":4,\"vvetrank\":17,\"vvetxp\":10320,\"wpnpu\":0}",
                "matchstartdate": 1738951595
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 5975627,
                "resulttype": 1,
                "teamid": 1,
                "race_id": 4,
                "xpgained": 24429,
                "counters": "{\"abil\":84,\"blost\":12,\"bprod\":21,\"cabil\":8,\"cflags\":0,\"cpearn\":28,\"dmgdone\":34430,\"edeaths\":93,\"ekills\":166,\"erein\":57,\"fuelearn\":923,\"fuelmax\":194,\"fuelspnt\":875,\"gt\":2272,\"ismod\":0,\"manearn\":8642,\"manmax\":1233,\"manspnt\":8353,\"munearn\":1626,\"munmax\":258,\"munspnt\":1595,\"pcap\":12,\"plost\":7,\"popmax\":0,\"precap\":11,\"sqkilled\":16,\"sqlost\":14,\"sqprod\":17,\"svetrank\":3,\"svetxp\":2880,\"upg\":16,\"utypes\":10,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":6,\"vlost\":5,\"vp0\":0,\"vp1\":451,\"vprod\":5,\"vvetrank\":24,\"vvetxp\":18880,\"wpnpu\":8}",
                "matchstartdate": 1738951595
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 2629923,
                "resulttype": 0,
                "teamid": 0,
                "race_id": 2,
                "xpgained": 21118,
                "counters": "{\"abil\":69,\"blost\":6,\"bprod\":22,\"cabil\":1,\"cflags\":0,\"cpearn\":25,\"dmgdone\":27085,\"edeaths\":148,\"ekills\":144,\"erein\":86,\"fuelearn\":872,\"fuelmax\":457,\"fuelspnt\":435,\"gt\":2272,\"ismod\":0,\"manearn\":8281,\"manmax\":872,\"manspnt\":8249,\"munearn\":1320,\"munmax\":321,\"munspnt\":1230,\"pcap\":7,\"plost\":5,\"popmax\":0,\"precap\":2,\"sqkilled\":8,\"sqlost\":20,\"sqprod\":22,\"svetrank\":6,\"svetxp\":8650,\"upg\":11,\"utypes\":10,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":4,\"vlost\":7,\"vp0\":0,\"vp1\":451,\"vprod\":8,\"vvetrank\":13,\"vvetxp\":7760,\"wpnpu\":1}",
                "matchstartdate": 1738951595
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 3745878,
                "resulttype": 1,
                "teamid": 1,
                "race_id": 1,
                "xpgained": 25543,
                "counters": "{\"abil\":110,\"blost\":2,\"bprod\":15,\"cabil\":9,\"cflags\":0,\"cpearn\":28,\"dmgdone\":28517,\"edeaths\":125,\"ekills\":150,\"erein\":98,\"fuelearn\":912,\"fuelmax\":260,\"fuelspnt\":685,\"gt\":2272,\"ismod\":0,\"manearn\":8149,\"manmax\":1327,\"manspnt\":7213,\"munearn\":1614,\"munmax\":260,\"munspnt\":1430,\"pcap\":14,\"plost\":8,\"popmax\":0,\"precap\":10,\"sqkilled\":17,\"sqlost\":5,\"sqprod\":14,\"svetrank\":8,\"svetxp\":13080,\"upg\":12,\"utypes\":9,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":8,\"vlost\":2,\"vp0\":0,\"vp1\":451,\"vprod\":6,\"vvetrank\":13,\"vvetxp\":7720,\"wpnpu\":0}",
                "matchstartdate": 1738951595
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 91363,
                "resulttype": 0,
                "teamid": 0,
                "race_id": 2,
                "xpgained": 26254,
                "counters": "{\"abil\":33,\"blost\":2,\"bprod\":14,\"cabil\":5,\"cflags\":0,\"cpearn\":29,\"dmgdone\":30419,\"edeaths\":171,\"ekills\":137,\"erein\":102,\"fuelearn\":810,\"fuelmax\":245,\"fuelspnt\":785,\"gt\":2071,\"ismod\":0,\"manearn\":8463,\"manmax\":1174,\"manspnt\":8549,\"munearn\":1231,\"munmax\":317,\"munspnt\":1120,\"pcap\":11,\"plost\":10,\"popmax\":0,\"precap\":8,\"sqkilled\":7,\"sqlost\":19,\"sqprod\":19,\"svetrank\":6,\"svetxp\":7560,\"upg\":8,\"utypes\":11,\"vabnd\":1,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":10,\"vp0\":0,\"vp1\":451,\"vprod\":11,\"vvetrank\":16,\"vvetxp\":14949,\"wpnpu\":0}",
                "matchstartdate": 1738951595
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 5850752,
                "resulttype": 1,
                "teamid": 1,
                "race_id": 1,
                "xpgained": 21919,
                "counters": "{\"abil\":79,\"blost\":9,\"bprod\":28,\"cabil\":7,\"cflags\":0,\"cpearn\":25,\"dmgdone\":22710,\"edeaths\":172,\"ekills\":121,\"erein\":142,\"fuelearn\":912,\"fuelmax\":298,\"fuelspnt\":665,\"gt\":2272,\"ismod\":0,\"manearn\":8096,\"manmax\":795,\"manspnt\":8095,\"munearn\":1614,\"munmax\":223,\"munspnt\":1600,\"pcap\":6,\"plost\":3,\"popmax\":0,\"precap\":5,\"sqkilled\":14,\"sqlost\":7,\"sqprod\":15,\"svetrank\":5,\"svetxp\":7340,\"upg\":9,\"utypes\":11,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":4,\"vlost\":4,\"vp0\":0,\"vp1\":451,\"vprod\":5,\"vvetrank\":19,\"vvetxp\":12040,\"wpnpu\":0}",
                "matchstartdate": 1738951595
            }
        ],
        "matchhistorymember": [
            {
                "matchhistory_id": 384074602,
                "profile_id": 5975627,
                "race_id": 4,
                "statgroup_id": 9935847,
                "teamid": 1,
                "wins": 2,
                "losses": 0,
                "streak": 2,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 1055,
                "newrating": 1104,
                "reporttype": 1
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 91363,
                "race_id": 2,
                "statgroup_id": 69189,
                "teamid": 0,
                "wins": 175,
                "losses": 172,
                "streak": -2,
                "arbitration": 2,
                "outcome": 0,
                "oldrating": 1070,
                "newrating": 1053,
                "reporttype": 3
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 1452224,
                "race_id": 0,
                "statgroup_id": 3847295,
                "teamid": 0,
                "wins": 22,
                "losses": 25,
                "streak": -1,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 1081,
                "newrating": 1064,
                "reporttype": 1
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 2629923,
                "race_id": 2,
                "statgroup_id": 3847295,
                "teamid": 0,
                "wins": 22,
                "losses": 25,
                "streak": -1,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 1081,
                "newrating": 1064,
                "reporttype": 1
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 5850752,
                "race_id": 1,
                "statgroup_id": 9935847,
                "teamid": 1,
                "wins": 2,
                "losses": 0,
                "streak": 2,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 1055,
                "newrating": 1104,
                "reporttype": 1
            },
            {
                "matchhistory_id": 384074602,
                "profile_id": 3745878,
                "race_id": 1,
                "statgroup_id": 9935847,
                "teamid": 1,
                "wins": 2,
                "losses": 0,
                "streak": 2,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 1055,
                "newrating": 1104,
                "reporttype": 1
            }
        ]
    },
    {
        "id": 380736194,
        "creator_profile_id": 3314052,
        "mapname": "8p_whiteball_express",
        "maxplayers": 6,
        "matchtype_id": 3,
        "options": "eNozYPvGAAOMDGxAMrW0KL8glZGBiREkdKetuIjT+1gUTI0coxyIxINBQASILQriyzMyS1KTEnNy4lMrCopSi4sZBgMAAMaGENM=",
        "slotinfo": "eNrNV12TokYUzW/xVRNBUGCq9qGbbwTFrxmcVB4AAZFRFBDUrfz3KN2649q7mVRSU+kX7fZ2H/qew7lXutP6/Wtjm6Vh/BbomzD9LV40nhiO7fIc32rkhVvE6UaXGk+dVqMI3PXlK9VqhK5//YFuNTLXD3BM5m4SMyiDtzrsMrPcwl9Oj9s64tdzdBGvAzvIlMxdB9akjovzceAujvVhF8x9Xi+vg8KV3MJtPDUAALB9GZUMwAgY4JXtypPz9/MoC14FaCj4E4gj1R+O5WU9MdshjNA6HF0jEgjedBdvOHSAjtdn14AzBpM2RYShtkfSI4a8ZvN0gaI5ClSPGMKzfMVQBWB9jwEBqO9z/TTAmJ6oS3QA2wQP97ob9iUhPPjx+PKl8WeLwC9Ds1S3c8cv/Y1f+o5f6hu/7Gfwm0BjqVFanQLYZqv5Iy8LrUrGiC+ftpRHXrSEN+QJynAWkLhnQ3Eso3WPiQgYwRFKSzR/bfoEfcmRPIoQ97ZJxFhqi1Kv16UdEWMWNjmIRLNZsCQNwyWXIA0rEkHD8iVmu99bKAaWEek5PFczdZTPPkPKp7+aGUuqnvQDmfAcGiyGOsIAJyKGcMuntGLBA8bdQDz/WLVEzdI0RXUZ5k6zzAc8ifpET5o7YgixocDb3d/n8eTOMZ+i79xM4F0e+Ze1gbgSRe22/p4rfVDGyJOK5ZyE4UoeizBUM7ue/R6jNBwdYUgrJQJ/50nwnh2pvvLPTIfIX48VekKXuuOP/YDn0J/jOSkMrnnPptGMUAtyJ8b1huw56lRhMbdDMrfPtPOC30NbAwRu57MbxomoH3V9w4AJEWOzvN4D+EpFwuhnyRFhsNAnYCiMwFK4bvIW6V2PtSHGgCcyRlEm+B70EJB8jQ057CcD7dFP4FwEK6Pa7s3OKbGCLGpyefNlOA6ZwVmPl/2hZ83RfmtD3l8EycmUc20WHuJqt3Ug62a8eamXZ+3qR7/vxULelbQda+85+22VOEI3eV3EzGlOTRKbpg5+kfDSWzWp2m1xjbXvbK3jwYS0xs/z/u65CtRdW+xYM+MwXubQTCi3LSTtnsqbo1mHGVref1azu3yX4r6r2b3/WU82XlMHXEcsIRIJ3rSjF2mAZquS1C8Z3FTFtT/pEmu/nh0xxqYk9WRKWuQV1q9D7Mloj4vwO+J9oCd7AZEBSy4fTKfjwY5jXoso77zStguiy8/no70mJ80oauruhY43NwfrxbSTwGMcbUvBo7cM2Ou2IvpwOld6kWN88/V/6alsj6ZogbvTRPcDnsp8jqfqvRDnWWJMQODSE+0Ue1G/zEn99djUdbRRXW1IXgQnRxEbTEns4Sc9bR+j9Rc7JWBonT6LMYBH1EsvUZ2f6OWM4W5Y/D8hidLHnv3yboQ2vRLRc4RySqgfckw1cR8HQmKvV58z0+D2iM5hApK3yqtbzoY2oVf7p7r745e/AHTcEUg=",
        "description": "AUTOMATCH",
        "startgametime": 1734292004,
        "completiontime": 1734292558,
        "matchhistoryreportresults": [
            {
                "matchhistory_id": 380736194,
                "profile_id": 3745878,
                "resulttype": 1,
                "teamid": 0,
                "race_id": 2,
                "xpgained": 1712,
                "counters": "{\"abil\":3,\"blost\":0,\"bprod\":12,\"cabil\":1,\"cflags\":0,\"cpearn\":2,\"dmgdone\":1185,\"edeaths\":8,\"ekills\":5,\"erein\":5,\"fuelearn\":209,\"fuelmax\":109,\"fuelspnt\":190,\"gt\":519,\"ismod\":0,\"manearn\":2244,\"manmax\":440,\"manspnt\":2416,\"munearn\":389,\"munmax\":218,\"munspnt\":210,\"pcap\":7,\"plost\":0,\"popmax\":0,\"precap\":2,\"sqkilled\":0,\"sqlost\":1,\"sqprod\":8,\"svetrank\":0,\"svetxp\":0,\"upg\":6,\"utypes\":6,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":0,\"vlost\":1,\"vp0\":500,\"vp1\":408,\"vprod\":4,\"vvetrank\":0,\"vvetxp\":0,\"wpnpu\":0}",
                "matchstartdate": 1734292004
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 3314052,
                "resulttype": 0,
                "teamid": 1,
                "race_id": 4,
                "xpgained": 2222,
                "counters": "{\"abil\":5,\"blost\":1,\"bprod\":19,\"cabil\":0,\"cflags\":0,\"cpearn\":3,\"dmgdone\":4001,\"edeaths\":12,\"ekills\":19,\"erein\":5,\"fuelearn\":151,\"fuelmax\":111,\"fuelspnt\":60,\"gt\":519,\"ismod\":0,\"manearn\":2271,\"manmax\":489,\"manspnt\":2349,\"munearn\":204,\"munmax\":94,\"munspnt\":110,\"pcap\":3,\"plost\":1,\"popmax\":0,\"precap\":1,\"sqkilled\":0,\"sqlost\":2,\"sqprod\":6,\"svetrank\":1,\"svetxp\":720,\"upg\":5,\"utypes\":6,\"vabnd\":1,\"vcap\":0,\"version\":3,\"vkill\":0,\"vlost\":1,\"vp0\":500,\"vp1\":408,\"vprod\":1,\"vvetrank\":2,\"vvetxp\":1040,\"wpnpu\":0}",
                "matchstartdate": 1734292004
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 1100533,
                "resulttype": 1,
                "teamid": 0,
                "race_id": 0,
                "xpgained": 2714,
                "counters": "{\"abil\":7,\"blost\":0,\"bprod\":12,\"cabil\":0,\"cflags\":0,\"cpearn\":3,\"dmgdone\":3874,\"edeaths\":7,\"ekills\":24,\"erein\":7,\"fuelearn\":209,\"fuelmax\":139,\"fuelspnt\":90,\"gt\":519,\"ismod\":0,\"manearn\":2215,\"manmax\":696,\"manspnt\":2290,\"munearn\":389,\"munmax\":209,\"munspnt\":235,\"pcap\":5,\"plost\":1,\"popmax\":0,\"precap\":1,\"sqkilled\":3,\"sqlost\":0,\"sqprod\":7,\"svetrank\":0,\"svetxp\":0,\"upg\":2,\"utypes\":5,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":1,\"vlost\":0,\"vp0\":500,\"vp1\":408,\"vprod\":2,\"vvetrank\":1,\"vvetxp\":480,\"wpnpu\":0}",
                "matchstartdate": 1734292004
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 6496950,
                "resulttype": 0,
                "teamid": 1,
                "race_id": 1,
                "xpgained": 2550,
                "counters": "{\"abil\":5,\"blost\":0,\"bprod\":13,\"cabil\":1,\"cflags\":0,\"cpearn\":3,\"dmgdone\":833,\"edeaths\":21,\"ekills\":2,\"erein\":14,\"fuelearn\":151,\"fuelmax\":116,\"fuelspnt\":105,\"gt\":519,\"ismod\":0,\"manearn\":2366,\"manmax\":539,\"manspnt\":2321,\"munearn\":204,\"munmax\":125,\"munspnt\":95,\"pcap\":5,\"plost\":4,\"popmax\":0,\"precap\":1,\"sqkilled\":1,\"sqlost\":1,\"sqprod\":5,\"svetrank\":0,\"svetxp\":0,\"upg\":3,\"utypes\":3,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":1,\"vlost\":0,\"vp0\":500,\"vp1\":408,\"vprod\":0,\"vvetrank\":0,\"vvetxp\":0,\"wpnpu\":0}",
                "matchstartdate": 1734292004
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 5850752,
                "resulttype": 1,
                "teamid": 0,
                "race_id": 2,
                "xpgained": 2682,
                "counters": "{\"abil\":4,\"blost\":0,\"bprod\":12,\"cabil\":0,\"cflags\":0,\"cpearn\":3,\"dmgdone\":1460,\"edeaths\":19,\"ekills\":12,\"erein\":20,\"fuelearn\":209,\"fuelmax\":114,\"fuelspnt\":105,\"gt\":519,\"ismod\":0,\"manearn\":2267,\"manmax\":491,\"manspnt\":2229,\"munearn\":389,\"munmax\":257,\"munspnt\":300,\"pcap\":4,\"plost\":2,\"popmax\":0,\"precap\":2,\"sqkilled\":2,\"sqlost\":0,\"sqprod\":7,\"svetrank\":0,\"svetxp\":0,\"upg\":4,\"utypes\":6,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":2,\"vlost\":0,\"vp0\":500,\"vp1\":408,\"vprod\":3,\"vvetrank\":1,\"vvetxp\":480,\"wpnpu\":0}",
                "matchstartdate": 1734292004
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 4610197,
                "resulttype": 0,
                "teamid": 1,
                "race_id": 3,
                "xpgained": 1536,
                "counters": "{\"abil\":18,\"blost\":0,\"bprod\":11,\"cabil\":3,\"cflags\":0,\"cpearn\":3,\"dmgdone\":1503,\"edeaths\":10,\"ekills\":12,\"erein\":6,\"fuelearn\":151,\"fuelmax\":98,\"fuelspnt\":115,\"gt\":519,\"ismod\":0,\"manearn\":2334,\"manmax\":1094,\"manspnt\":2098,\"munearn\":204,\"munmax\":114,\"munspnt\":90,\"pcap\":1,\"plost\":0,\"popmax\":0,\"precap\":1,\"sqkilled\":0,\"sqlost\":2,\"sqprod\":9,\"svetrank\":1,\"svetxp\":530,\"upg\":4,\"utypes\":8,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":0,\"vlost\":2,\"vp0\":500,\"vp1\":408,\"vprod\":4,\"vvetrank\":0,\"vvetxp\":0,\"wpnpu\":0}",
                "matchstartdate": 1734292004
            }
        ],
        "matchhistorymember": [
            {
                "matchhistory_id": 380736194,
                "profile_id": 3314052,
                "race_id": 4,
                "statgroup_id": 9810305,
                "teamid": 1,
                "wins": 51,
                "losses": 71,
                "streak": -1,
                "arbitration": 2,
                "outcome": 0,
                "oldrating": 798,
                "newrating": 786,
                "reporttype": 3
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 1100533,
                "race_id": 0,
                "statgroup_id": 10152026,
                "teamid": 0,
                "wins": 3,
                "losses": 0,
                "streak": 3,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 876,
                "newrating": 912,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 5850752,
                "race_id": 2,
                "statgroup_id": 10152026,
                "teamid": 0,
                "wins": 3,
                "losses": 0,
                "streak": 3,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 876,
                "newrating": 912,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 3745878,
                "race_id": 2,
                "statgroup_id": 10152026,
                "teamid": 0,
                "wins": 3,
                "losses": 0,
                "streak": 3,
                "arbitration": 1,
                "outcome": 1,
                "oldrating": 876,
                "newrating": 912,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 4610197,
                "race_id": 3,
                "statgroup_id": 9810305,
                "teamid": 1,
                "wins": 51,
                "losses": 71,
                "streak": -1,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 798,
                "newrating": 786,
                "reporttype": 1
            },
            {
                "matchhistory_id": 380736194,
                "profile_id": 6496950,
                "race_id": 1,
                "statgroup_id": 9810305,
                "teamid": 1,
                "wins": 51,
                "losses": 71,
                "streak": -1,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 798,
                "newrating": 786,
                "reporttype": 1
            }
        ]
    },
    ]

def _dummy_database_profiles():
    return [
    {
        "profile_id": 710149,
        "name": "/steam/76561198072580481",
        "alias": "Servo",
        "personal_statgroup_id": 704920,
        "xp": 18785964,
        "level": 300,
        "leaderboardregion_id": 0,
        "country": "be"
    },
    {
        "profile_id": 1027269,
        "name": "/steam/76561198090749128",
        "alias": "Fritz",
        "personal_statgroup_id": 1024345,
        "xp": 18785964,
        "level": 300,
        "leaderboardregion_id": 0,
        "country": "de"
    },
    {
        "profile_id": 413238,
        "name": "/steam/76561197981443937",
        "alias": "TheRegulator",
        "personal_statgroup_id": 403225,
        "xp": 18785964,
        "level": 300,
        "leaderboardregion_id": 0,
        "country": "dk"
    },
    ]

# def _dummy_database_profiles():



@pytest.fixture
def mock_games():
    games = GamesList(_dummy_database_matches, _dummy_database_profiles)
    return games



def test_datetime_duration(mock_games: GamesList):

    match = {"startgametime": 1733426285,
        "completiontime": 1733427773,}
    
    result = mock_games._get_game_duration(match, 'datetime')
    assert result == {"hours": 0, "minutes": 24}








class TestSorting:

    @pytest.fixture
    def last_games(self):
        return [
            {"start_timestamp": 1738354960,"mapname": "4p_belgorod"},
            {"start_timestamp": 1738782821,"mapname": "6p_foy"},
            {"start_timestamp": 1734892194,"mapname": "wolfheze"}
            ]
    


    def test_sorting_reversed(self, mock_games: GamesList, last_games):        

        mock_games.sort_games(last_games, sort_by='start_timestamp')

        assert mock_games.last_games_filtered[0]["start_timestamp"] == 1738782821
        assert mock_games.last_games_filtered[1]["start_timestamp"] == 1738354960
        assert mock_games.last_games_filtered[2]["start_timestamp"] == 1734892194



    def test_sorting_not_reversed(self, mock_games: GamesList, last_games):        

        mock_games.sort_games(last_games, sort_by='start_timestamp', reverse=False)

        assert mock_games.last_games_filtered[0]["start_timestamp"] == 1734892194
        assert mock_games.last_games_filtered[1]["start_timestamp"] == 1738354960
        assert mock_games.last_games_filtered[2]["start_timestamp"] == 1738782821




    def test_sorting_not_strings_reversed(self, mock_games: GamesList, last_games):        

        mock_games.sort_games(last_games, sort_by="mapname")

        assert mock_games.last_games_filtered[0]["mapname"] == "wolfheze"
        assert mock_games.last_games_filtered[1]["mapname"] == "6p_foy"
        assert mock_games.last_games_filtered[2]["mapname"] == "4p_belgorod"
        assert mock_games.saved__sort_by == "mapname"



    def test_sorting_reversed_saved(self, mock_games: GamesList, last_games):        

        mock_games.saved__sort_by = 'start_timestamp'

        mock_games.sort_games(last_games)

        assert mock_games.last_games_filtered[0]["start_timestamp"] == 1738782821
        assert mock_games.last_games_filtered[1]["start_timestamp"] == 1738354960
        assert mock_games.last_games_filtered[2]["start_timestamp"] == 1734892194







class TestGetFormat:

    def test_2v2(self, mock_games):

        match = {"matchhistoryreportresults": 
                [
                    {"profile_id": 1}, 
                    {"profile_id": 2},
                    {"profile_id": 3},
                    {"profile_id": 4}
                ]
                }
        
        result = mock_games._get_game_format(match)
        assert result == 2



    def test_iregular(self, mock_games):

        match = {"matchhistoryreportresults": 
                [
                    {"profile_id": 1}, 
                    {"profile_id": 2},
                    {"profile_id": 3},
                    {"profile_id": 5},
                    {"profile_id": 4}
                ]
                }
        
        result = mock_games._get_game_format(match)
        assert result == 3
    


def test_convert_time(mock_games):

    match = {"startgametime": 1739214314}
    result = mock_games._convert_time(match)

    assert result == {
            "year": 2025,
            "month": 2,
            "day": 10,
            "hour": 19,
            "minute": 5
        }



class TestGetHistorySimplified:

    def dummy_get_response(self, player_id):
        pass


    def test_lenght(self, mock_games, monkeypatch: pytest.MonkeyPatch):

        # monkeypatch.setattr(data, "_get_response", self.dummy_get_response)
        
        last_games = mock_games.get_history_simplified(do_update_databse=False)


        assert len(last_games) == 4



@pytest.mark.parametrize("player_id, alias", [
(710149, "Servo"),
(1027269, "Fritz"),
(413238, "TheRegulator"),
(111, None),
])
def test_get_player_name(mock_games, player_id, alias):

    result = mock_games._get_player_name(player_id)
    assert result == alias



class TestGetPlayers:

    @pytest.fixture
    def match_members(self):
        return {
                    "matchhistoryreportresults": [
                {
                    "matchhistory_id": 383702785,
                    "profile_id": 710149,
                    "resulttype": 1,
                    "teamid": 0,
                    "race_id": 1,
                    "xpgained": 21417,
                    "counters": "{\"abil\":69,\"blost\":5,\"bprod\":38,\"cabil\":4,\"cflags\":0,\"cpearn\":24,\"dmgdone\":38289,\"edeaths\":122,\"ekills\":124,\"erein\":110,\"fuelearn\":782,\"fuelmax\":151,\"fuelspnt\":745,\"gt\":1988,\"ismod\":0,\"manearn\":7353,\"manmax\":1304,\"manspnt\":7073,\"munearn\":1230,\"munmax\":163,\"munspnt\":1160,\"pcap\":23,\"plost\":18,\"popmax\":0,\"precap\":23,\"sqkilled\":13,\"sqlost\":4,\"sqprod\":14,\"svetrank\":8,\"svetxp\":12520,\"upg\":9,\"utypes\":10,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":3,\"vp0\":209,\"vp1\":0,\"vprod\":5,\"vvetrank\":18,\"vvetxp\":13140,\"wpnpu\":0}",
                    "matchstartdate": 1738442136
                },
                {
                    "matchhistory_id": 383702785,
                    "profile_id": 1027269,
                    "resulttype": 0,
                    "teamid": 1,
                    "race_id": 2,
                    "xpgained": 16808,
                    "counters": "{\"abil\":82,\"blost\":4,\"bprod\":16,\"cabil\":1,\"cflags\":0,\"cpearn\":20,\"dmgdone\":22406,\"edeaths\":114,\"ekills\":99,\"erein\":69,\"fuelearn\":804,\"fuelmax\":271,\"fuelspnt\":755,\"gt\":1988,\"ismod\":0,\"manearn\":7932,\"manmax\":1073,\"manspnt\":7773,\"munearn\":1234,\"munmax\":231,\"munspnt\":1010,\"pcap\":21,\"plost\":17,\"popmax\":0,\"precap\":17,\"sqkilled\":4,\"sqlost\":11,\"sqprod\":18,\"svetrank\":6,\"svetxp\":8620,\"upg\":14,\"utypes\":11,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":2,\"vlost\":3,\"vp0\":209,\"vp1\":0,\"vprod\":10,\"vvetrank\":16,\"vvetxp\":11640,\"wpnpu\":1}",
                    "matchstartdate": 1738442136
                },
                {
                    "matchhistory_id": 383702785,
                    "profile_id": 413238,
                    "resulttype": 1,
                    "teamid": 0,
                    "race_id": 3,
                    "xpgained": 18758,
                    "counters": "{\"abil\":83,\"blost\":5,\"bprod\":21,\"cabil\":4,\"cflags\":0,\"cpearn\":21,\"dmgdone\":26810,\"edeaths\":167,\"ekills\":86,\"erein\":132,\"fuelearn\":782,\"fuelmax\":336,\"fuelspnt\":580,\"gt\":1988,\"ismod\":0,\"manearn\":7377,\"manmax\":778,\"manspnt\":7353,\"munearn\":1230,\"munmax\":214,\"munspnt\":1221,\"pcap\":20,\"plost\":16,\"popmax\":0,\"precap\":14,\"sqkilled\":5,\"sqlost\":10,\"sqprod\":13,\"svetrank\":2,\"svetxp\":7060,\"upg\":9,\"utypes\":10,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":2,\"vlost\":3,\"vp0\":209,\"vp1\":0,\"vprod\":5,\"vvetrank\":18,\"vvetxp\":10540,\"wpnpu\":0}",
                    "matchstartdate": 1738442136
                },
                {
                    "matchhistory_id": 383702785,
                    "profile_id": 1027269,
                    "resulttype": 0,
                    "teamid": 1,
                    "race_id": 0,
                    "xpgained": 21297,
                    "counters": "{\"abil\":61,\"blost\":1,\"bprod\":16,\"cabil\":2,\"cflags\":0,\"cpearn\":24,\"dmgdone\":26836,\"edeaths\":102,\"ekills\":184,\"erein\":74,\"fuelearn\":804,\"fuelmax\":241,\"fuelspnt\":645,\"gt\":1988,\"ismod\":0,\"manearn\":7225,\"manmax\":1214,\"manspnt\":7220,\"munearn\":1210,\"munmax\":359,\"munspnt\":1000,\"pcap\":23,\"plost\":20,\"popmax\":0,\"precap\":17,\"sqkilled\":9,\"sqlost\":8,\"sqprod\":14,\"svetrank\":4,\"svetxp\":8270,\"upg\":12,\"utypes\":11,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":3,\"vlost\":2,\"vp0\":209,\"vp1\":0,\"vprod\":5,\"vvetrank\":17,\"vvetxp\":11080,\"wpnpu\":0}",
                    "matchstartdate": 1738442136
                }
            ],
        }



    def test_number_of_players(self, mock_games, match_members):

        result = mock_games._get_players(match_members, team = 0)
        assert len(result) == 2



    # @pytest.mark.parametrize("name, faction", [
    # ("sergu", 1),
    # ("Karl", 2),
    # ("Ing", 1),
    # ("Fritz", 0),
    # ])
    # @pytest.mark
    def test_data_faction_of_players(self, mock_games, match_members):

        result = mock_games._get_players(match_members, team = 0)
        assert result[0]['faction'] == Factions.Soviet.name
        assert result[1]['faction'] == Factions.USF.name



    def test_data_names_of_players(self, mock_games, match_members):

        result = mock_games._get_players(match_members, team = 0)
        assert result[0]['name'] == 'Servo'
        assert result[1]['name'] == 'TheRegulator'




@pytest.mark.parametrize("race_id, faction_name", [
    (0, Factions.OST.name),
    (1, Factions.Soviet.name),
    (2, Factions.OKW.name),
    (3, Factions.USF.name),
    (4, Factions.UKF.name),
])
def test_race_id_to_name(mock_games, race_id, faction_name):

    result = mock_games._race_id_to_name(race_id)
    assert result == faction_name



@pytest.mark.parametrize("old_match_type, converted_type", [
    ("AUTOMATCH", "Automatch"),
    ("SESSION_MATCH_KEY", "Custom")
])
def test_get_match_type(mock_games, old_match_type, converted_type):

    result = mock_games._get_match_type(old_match_type)
    assert result == converted_type




class TestFilterGames:

    def test_filter_games(self, mock_games: GamesList):

        mock_games.get_history_simplified(do_update_databse=False)
        mock_games.filter_games(filter_category="gametype", filter_by="Automatch")

        assert len(mock_games.last_games_filtered) == 3



    def test_filter_games_nested(self, mock_games: GamesList):
        
        mock_games.get_history_simplified(do_update_databse=False)
        mock_games.filter_games(filter_category="startgametime", filter_sub_category="year", filter_by=2024) #Kamil9132

        assert len(mock_games.last_games_filtered) == 2



    def test_filter_games_saved(self, mock_games: GamesList):

        mock_games.get_history_simplified(do_update_databse=False)

        mock_games.saved__filter_category = "gameformat"
        mock_games.saved__filter_by = 2

        mock_games.filter_games() #Kamil9132

        assert len(mock_games.last_games_filtered) == 1



    def test_filter_games_saved_2(self, mock_games: GamesList):

        mock_games.filter_games(filter_category="gameformat", filter_by = 3)


        mock_games.get_history_simplified(do_update_databse=False)


        mock_games.filter_games() #Kamil9132

        assert len(mock_games.last_games_filtered) == 3



# def test_get_players_team_0(mock_games: GamesList):
#     result = mock_games._get_players(_match(), 0)

#     assert len(result) == 2

#     for i in result:
#         i





    

