from datetime import datetime
from games import Games
import pytest
import data


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
        "observertotal": 0,
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
        "matchhistoryitems": [
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 430727895,
                "itemdefinition_id": 6000,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 440588963,
                "itemdefinition_id": 6892,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 498982197,
                "itemdefinition_id": 396479,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 526955437,
                "itemdefinition_id": 396501,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 559043863,
                "itemdefinition_id": 396503,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 566005706,
                "itemdefinition_id": 396500,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 62977806,
                "itemdefinition_id": 7546,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 346033873,
                "itemdefinition_id": 452461,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 572153251,
                "itemdefinition_id": 5925,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 436581524,
                "itemdefinition_id": 387935,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 442358484,
                "itemdefinition_id": 6111,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1428013,
                "matchhistory_id": 380940866,
                "iteminstance_id": 442735913,
                "itemdefinition_id": 6101,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 138584540,
                "itemdefinition_id": 7258,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 207772937,
                "itemdefinition_id": 396476,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 233203434,
                "itemdefinition_id": 7257,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 236025025,
                "itemdefinition_id": 396477,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 238118765,
                "itemdefinition_id": 396475,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 265990417,
                "itemdefinition_id": 7259,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 132855813,
                "itemdefinition_id": 5580,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 167422057,
                "itemdefinition_id": 5925,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 223134566,
                "itemdefinition_id": 5926,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 147871188,
                "itemdefinition_id": 5909,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 148861258,
                "itemdefinition_id": 396521,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 233705693,
                "itemdefinition_id": 388789,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 148861257,
                "itemdefinition_id": 7328,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 5
            },
            {
                "profile_id": 1814861,
                "matchhistory_id": 380940866,
                "iteminstance_id": 440515074,
                "itemdefinition_id": 261085,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 6
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 198469475,
                "itemdefinition_id": 450814,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 198469476,
                "itemdefinition_id": 450815,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 198469477,
                "itemdefinition_id": 450816,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 396581972,
                "itemdefinition_id": 6001,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 434863074,
                "itemdefinition_id": 450767,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 569806413,
                "itemdefinition_id": 396501,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 163689242,
                "itemdefinition_id": 6121,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 163689244,
                "itemdefinition_id": 5575,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 163689258,
                "itemdefinition_id": 6119,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 163689234,
                "itemdefinition_id": 5913,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 572151087,
                "itemdefinition_id": 387936,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 572638282,
                "itemdefinition_id": 396522,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 2013306,
                "matchhistory_id": 380940866,
                "iteminstance_id": 195838737,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380940866,
                "iteminstance_id": 554777001,
                "itemdefinition_id": 7537,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380940866,
                "iteminstance_id": 554777005,
                "itemdefinition_id": 5928,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380940866,
                "iteminstance_id": 554777006,
                "itemdefinition_id": 5929,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380940866,
                "iteminstance_id": 337269263,
                "itemdefinition_id": 5913,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380940866,
                "iteminstance_id": 499641999,
                "itemdefinition_id": 6111,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380940866,
                "iteminstance_id": 555230961,
                "itemdefinition_id": 6110,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 524864589,
                "itemdefinition_id": 6902,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 524864590,
                "itemdefinition_id": 6901,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 524864594,
                "itemdefinition_id": 5997,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 554719387,
                "itemdefinition_id": 396433,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 570323370,
                "itemdefinition_id": 396431,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 570323371,
                "itemdefinition_id": 396432,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 499561517,
                "itemdefinition_id": 5572,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 517658096,
                "itemdefinition_id": 5568,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 517658119,
                "itemdefinition_id": 5928,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 503975427,
                "itemdefinition_id": 6101,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 516379396,
                "itemdefinition_id": 388397,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380940866,
                "iteminstance_id": 582025166,
                "itemdefinition_id": 5863,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 561116064,
                "itemdefinition_id": 347668,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 568012709,
                "itemdefinition_id": 347662,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 556202043,
                "itemdefinition_id": 257800,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 556202056,
                "itemdefinition_id": 450495,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 556202058,
                "itemdefinition_id": 450494,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 554772781,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 556641471,
                "itemdefinition_id": 259230,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 557206874,
                "itemdefinition_id": 259274,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 380940866,
                "iteminstance_id": 582513529,
                "itemdefinition_id": 260896,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 6
            }
        ],
        "matchurls": [],
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
        "observertotal": 0,
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
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 5850752,
                "resulttype": 0,
                "teamid": 0,
                "race_id": 1,
                "xpgained": 9574,
                "counters": "{\"abil\":83,\"blost\":3,\"bprod\":17,\"cabil\":1,\"cflags\":0,\"cpearn\":12,\"dmgdone\":13914,\"edeaths\":90,\"ekills\":40,\"erein\":63,\"fuelearn\":595,\"fuelmax\":255,\"fuelspnt\":580,\"gt\":1632,\"ismod\":0,\"manearn\":6289,\"manmax\":1177,\"manspnt\":6547,\"munearn\":980,\"munmax\":382,\"munspnt\":636,\"pcap\":3,\"plost\":1,\"popmax\":0,\"precap\":3,\"sqkilled\":2,\"sqlost\":4,\"sqprod\":16,\"svetrank\":3,\"svetxp\":3040,\"upg\":7,\"utypes\":7,\"vabnd\":0,\"vcap\":0,\"version\":3,\"vkill\":1,\"vlost\":2,\"vp0\":0,\"vp1\":416,\"vprod\":7,\"vvetrank\":12,\"vvetxp\":5200,\"wpnpu\":0}",
                "matchstartdate": 1738613003
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 5975627,
                "resulttype": 1,
                "teamid": 1,
                "race_id": 3,
                "xpgained": 11855,
                "counters": "{\"abil\":58,\"blost\":1,\"bprod\":17,\"cabil\":5,\"cflags\":0,\"cpearn\":15,\"dmgdone\":12135,\"edeaths\":80,\"ekills\":105,\"erein\":74,\"fuelearn\":698,\"fuelmax\":266,\"fuelspnt\":515,\"gt\":1632,\"ismod\":0,\"manearn\":5878,\"manmax\":971,\"manspnt\":5725,\"munearn\":1117,\"munmax\":265,\"munspnt\":955,\"pcap\":9,\"plost\":6,\"popmax\":0,\"precap\":6,\"sqkilled\":6,\"sqlost\":3,\"sqprod\":12,\"svetrank\":2,\"svetxp\":1410,\"upg\":7,\"utypes\":15,\"vabnd\":0,\"vcap\":3,\"version\":3,\"vkill\":4,\"vlost\":2,\"vp0\":0,\"vp1\":416,\"vprod\":4,\"vvetrank\":11,\"vvetxp\":6160,\"wpnpu\":10}",
                "matchstartdate": 1738613003
            }
        ],
        "matchhistoryitems": [
            {
                "profile_id": 1100533,
                "matchhistory_id": 383842535,
                "iteminstance_id": 562653664,
                "itemdefinition_id": 7247,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 383842535,
                "iteminstance_id": 276611704,
                "itemdefinition_id": 5916,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 383842535,
                "iteminstance_id": 408170435,
                "itemdefinition_id": 396521,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 383842535,
                "iteminstance_id": 564236259,
                "itemdefinition_id": 6103,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 383842535,
                "iteminstance_id": 499329239,
                "itemdefinition_id": 452455,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 383842535,
                "iteminstance_id": 337269242,
                "itemdefinition_id": 450206,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 383842535,
                "iteminstance_id": 337269276,
                "itemdefinition_id": 450226,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 383842535,
                "iteminstance_id": 516398038,
                "itemdefinition_id": 450249,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 4540940,
                "matchhistory_id": 383842535,
                "iteminstance_id": 405261738,
                "itemdefinition_id": 6116,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 4540940,
                "matchhistory_id": 383842535,
                "iteminstance_id": 406518341,
                "itemdefinition_id": 6103,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 4540940,
                "matchhistory_id": 383842535,
                "iteminstance_id": 407499209,
                "itemdefinition_id": 6110,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 4540940,
                "matchhistory_id": 383842535,
                "iteminstance_id": 408484612,
                "itemdefinition_id": 6112,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 501503052,
                "itemdefinition_id": 396490,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 503546106,
                "itemdefinition_id": 6896,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 504153479,
                "itemdefinition_id": 6001,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 511337084,
                "itemdefinition_id": 396481,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 511732008,
                "itemdefinition_id": 6895,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 512497032,
                "itemdefinition_id": 396482,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 517658110,
                "itemdefinition_id": 7543,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 503975427,
                "itemdefinition_id": 6101,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 504497733,
                "itemdefinition_id": 388789,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 383842535,
                "iteminstance_id": 582025166,
                "itemdefinition_id": 5863,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 383842535,
                "iteminstance_id": 556202045,
                "itemdefinition_id": 450482,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 383842535,
                "iteminstance_id": 554772781,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 383842535,
                "iteminstance_id": 556641471,
                "itemdefinition_id": 259230,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 383842535,
                "iteminstance_id": 559874629,
                "itemdefinition_id": 394328,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6576746,
                "matchhistory_id": 383842535,
                "iteminstance_id": 570728873,
                "itemdefinition_id": 186414,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 6576746,
                "matchhistory_id": 383842535,
                "iteminstance_id": 570728857,
                "itemdefinition_id": 259078,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6576746,
                "matchhistory_id": 383842535,
                "iteminstance_id": 570728898,
                "itemdefinition_id": 259252,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6576746,
                "matchhistory_id": 383842535,
                "iteminstance_id": 570851740,
                "itemdefinition_id": 259253,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            }
        ],
        "matchurls": [],
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
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 4540940,
                "race_id": 0,
                "statgroup_id": 6824297,
                "teamid": 0,
                "wins": 8,
                "losses": 5,
                "streak": -1,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 1117,
                "newrating": 1090,
                "reporttype": 1
            },
            {
                "matchhistory_id": 383842535,
                "profile_id": 5850752,
                "race_id": 1,
                "statgroup_id": 8636562,
                "teamid": 0,
                "wins": 50,
                "losses": 64,
                "streak": -2,
                "arbitration": 1,
                "outcome": 0,
                "oldrating": 885,
                "newrating": 870,
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
        "observertotal": 0,
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
        "matchhistoryitems": [
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 47595363,
                "itemdefinition_id": 347660,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 198964716,
                "itemdefinition_id": 450808,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 198964718,
                "itemdefinition_id": 450810,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 531842181,
                "itemdefinition_id": 450860,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 533842083,
                "itemdefinition_id": 450861,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 575251215,
                "itemdefinition_id": 450862,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 3535496,
                "itemdefinition_id": 186419,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 570196479,
                "itemdefinition_id": 450494,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 3
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 576342159,
                "itemdefinition_id": 259929,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 533620474,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 540193946,
                "itemdefinition_id": 348149,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 567532771,
                "itemdefinition_id": 259746,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 579842680,
                "itemdefinition_id": 451456,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 5
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 570328502,
                "itemdefinition_id": 260906,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 6
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 3535506,
                "itemdefinition_id": 5874,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 3535508,
                "itemdefinition_id": 5875,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 21440740,
                "itemdefinition_id": 7250,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 21479995,
                "itemdefinition_id": 6919,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 91363,
                "matchhistory_id": 384074602,
                "iteminstance_id": 198964711,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 210969874,
                "itemdefinition_id": 396431,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 347956351,
                "itemdefinition_id": 6902,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 347956352,
                "itemdefinition_id": 6901,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 347956353,
                "itemdefinition_id": 5997,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 348538251,
                "itemdefinition_id": 396433,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 350577895,
                "itemdefinition_id": 396444,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 74459694,
                "itemdefinition_id": 5570,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 212898127,
                "itemdefinition_id": 5568,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 347956358,
                "itemdefinition_id": 5929,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 74543954,
                "itemdefinition_id": 6100,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"levelup\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 335960109,
                "itemdefinition_id": 6101,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 350428591,
                "itemdefinition_id": 388397,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 76381241,
                "itemdefinition_id": 261162,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 6
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 74459690,
                "itemdefinition_id": 7250,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 74459698,
                "itemdefinition_id": 6919,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 74459704,
                "itemdefinition_id": 5874,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 74459706,
                "itemdefinition_id": 5875,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 9
            },
            {
                "profile_id": 1452224,
                "matchhistory_id": 384074602,
                "iteminstance_id": 122611845,
                "itemdefinition_id": 450104,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 8
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 344543397,
                "itemdefinition_id": 450748,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 348735817,
                "itemdefinition_id": 347671,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 261001245,
                "itemdefinition_id": 186417,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 261001249,
                "itemdefinition_id": 186418,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 347926855,
                "itemdefinition_id": 259929,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 261001273,
                "itemdefinition_id": 259078,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 346715757,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 398567677,
                "itemdefinition_id": 259098,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 348728214,
                "itemdefinition_id": 451452,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 5
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 348482123,
                "itemdefinition_id": 260900,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 6
            },
            {
                "profile_id": 2629923,
                "matchhistory_id": 384074602,
                "iteminstance_id": 261001289,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 337269248,
                "itemdefinition_id": 6119,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 554777011,
                "itemdefinition_id": 5923,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 554777012,
                "itemdefinition_id": 5924,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 337269263,
                "itemdefinition_id": 5913,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 499641999,
                "itemdefinition_id": 6111,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 555230961,
                "itemdefinition_id": 6110,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 384074602,
                "iteminstance_id": 337269277,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 501503052,
                "itemdefinition_id": 396490,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 503546106,
                "itemdefinition_id": 6896,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 504153479,
                "itemdefinition_id": 6001,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 511337084,
                "itemdefinition_id": 396481,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 511732008,
                "itemdefinition_id": 6895,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 512497032,
                "itemdefinition_id": 396482,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 499561471,
                "itemdefinition_id": 5580,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 499561491,
                "itemdefinition_id": 6119,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 517658125,
                "itemdefinition_id": 5924,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 503975427,
                "itemdefinition_id": 6101,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 504497733,
                "itemdefinition_id": 388789,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 384074602,
                "iteminstance_id": 582025166,
                "itemdefinition_id": 5863,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 511131157,
                "itemdefinition_id": 452455,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 511131164,
                "itemdefinition_id": 450075,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 556202044,
                "itemdefinition_id": 450286,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 511131133,
                "itemdefinition_id": 450206,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 511131172,
                "itemdefinition_id": 450226,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 564430668,
                "itemdefinition_id": 450224,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5975627,
                "matchhistory_id": 384074602,
                "iteminstance_id": 566380383,
                "itemdefinition_id": 450322,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 6
            }
        ],
        "matchurls": [],
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
        "observertotal": 0,
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
        "matchhistoryitems": [
            {
                "profile_id": 1100533,
                "matchhistory_id": 380736194,
                "iteminstance_id": 276611717,
                "itemdefinition_id": 5572,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562653681,
                "itemdefinition_id": 7554,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562653683,
                "itemdefinition_id": 5927,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 380736194,
                "iteminstance_id": 566103490,
                "itemdefinition_id": 5814,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 380736194,
                "iteminstance_id": 566103514,
                "itemdefinition_id": 387938,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 1100533,
                "matchhistory_id": 380736194,
                "iteminstance_id": 566793660,
                "itemdefinition_id": 5859,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 489084104,
                "itemdefinition_id": 450857,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 565806977,
                "itemdefinition_id": 450384,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 566993261,
                "itemdefinition_id": 450378,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 568505537,
                "itemdefinition_id": 450572,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 568572585,
                "itemdefinition_id": 450587,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 311554273,
                "itemdefinition_id": 450075,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 311554276,
                "itemdefinition_id": 450074,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 353272300,
                "itemdefinition_id": 452455,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 485293639,
                "itemdefinition_id": 450205,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 487067936,
                "itemdefinition_id": 450290,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 577730436,
                "itemdefinition_id": 450282,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 502534438,
                "itemdefinition_id": 451455,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 5
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 311554257,
                "itemdefinition_id": 349043,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 6
            },
            {
                "profile_id": 3314052,
                "matchhistory_id": 380736194,
                "iteminstance_id": 311554293,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 337269250,
                "itemdefinition_id": 186417,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 554776988,
                "itemdefinition_id": 450495,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 554776990,
                "itemdefinition_id": 450494,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 337269237,
                "itemdefinition_id": 259078,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 499835430,
                "itemdefinition_id": 259230,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 569960605,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 3745878,
                "matchhistory_id": 380736194,
                "iteminstance_id": 337269277,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 568578850,
                "itemdefinition_id": 450311,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 579663347,
                "itemdefinition_id": 346748,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 581419329,
                "itemdefinition_id": 450781,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 411184133,
                "itemdefinition_id": 186415,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 411184145,
                "itemdefinition_id": 452456,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 582649646,
                "itemdefinition_id": 260696,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 411184118,
                "itemdefinition_id": 259078,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 563560938,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 568370982,
                "itemdefinition_id": 395922,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"achievement\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 568370979,
                "itemdefinition_id": 404727,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"achievement\":1}",
                "itemlocation_id": 5
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 564367280,
                "itemdefinition_id": 260906,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 6
            },
            {
                "profile_id": 4610197,
                "matchhistory_id": 380736194,
                "iteminstance_id": 411184163,
                "itemdefinition_id": 450787,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 8
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380736194,
                "iteminstance_id": 499561497,
                "itemdefinition_id": 186419,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380736194,
                "iteminstance_id": 499561511,
                "itemdefinition_id": 452452,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380736194,
                "iteminstance_id": 517658090,
                "itemdefinition_id": 257800,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380736194,
                "iteminstance_id": 499788754,
                "itemdefinition_id": 259230,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380736194,
                "iteminstance_id": 567064168,
                "itemdefinition_id": 259253,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 5850752,
                "matchhistory_id": 380736194,
                "iteminstance_id": 568377045,
                "itemdefinition_id": 259099,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562656136,
                "itemdefinition_id": 6003,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562952055,
                "itemdefinition_id": 396479,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 563179403,
                "itemdefinition_id": 450772,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 565346232,
                "itemdefinition_id": 450769,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 566652063,
                "itemdefinition_id": 450761,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 2
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562632581,
                "itemdefinition_id": 5580,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562632595,
                "itemdefinition_id": 6119,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 567694679,
                "itemdefinition_id": 7247,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{}",
                "itemlocation_id": 3
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562632606,
                "itemdefinition_id": 5916,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562632614,
                "itemdefinition_id": 5913,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 563325826,
                "itemdefinition_id": 6112,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "",
                "itemlocation_id": 4
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562632608,
                "itemdefinition_id": 347819,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 5
            },
            {
                "profile_id": 6496950,
                "matchhistory_id": 380736194,
                "iteminstance_id": 562632603,
                "itemdefinition_id": 349043,
                "durabilitytype": 0,
                "durability": 1,
                "metadata": "{\"dlc\":1}",
                "itemlocation_id": 6
            }
        ],
        "matchurls": [],
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
    games = Games(_dummy_database_matches, _dummy_database_profiles)
    return games



def test_datetime_duration(mock_games: Games):

    match = {"startgametime": 1733426285,
        "completiontime": 1733427773,}
    
    result = mock_games._get_game_duration(match, 'datetime')
    assert result == {"hours": 0, "minutes": 24}



def test_sorting(mock_games: Games):
    games = [
        {       "startgametime": {
            "year": 2025,
            "month": 1,
            "day": 31,
            "hour": 20,
            "minute": 22
        },
        "start_timestamp": 1738354960,},

        {        "startgametime": {
            "year": 2025,
            "month": 2,
            "day": 5,
            "hour": 19,
            "minute": 13
        },
        "start_timestamp": 1738782821,},

        {        "startgametime": {
            "year": 2024,
            "month": 12,
            "day": 22,
            "hour": 18,
            "minute": 29
        },
        "start_timestamp": 1734892194,}]

    mock_games.sort_games(games)

    assert mock_games.last_games[0]["start_timestamp"] == 1738782821
    assert mock_games.last_games[1]["start_timestamp"] == 1738354960
    assert mock_games.last_games[2]["start_timestamp"] == 1734892194



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

    def test_lenght(self, mock_games):
        
        mock_games.get_history_simplified()

        last_games = mock_games.last_games

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



# def test_get_players_team_0(mock_games: Games):
#     result = mock_games._get_players(_match(), 0)

#     assert len(result) == 2

#     for i in result:
#         i





    

