from lxml import html
import requests
from decimal import *
getcontext().prec = 2
page = requests.get('https://www.road-results.com/?n=results&sn=upgrades')
tree = html.fromstring(page.content)
upgrades_tree = tree.xpath('//*[@id="upgradeboard"]/table/tr[*]/td[2]/text()')
regions_tree = tree.xpath('//*[@id="upgradeboard"]/table/tr[*]/td[4]/text()')
upgrade_dict = {}
for upgrade, region in zip(upgrades_tree, regions_tree):
    readable_upgrade = (int(upgrade[0]), int(upgrade[2]))
    if (readable_upgrade, region) not in upgrade_dict:
        upgrade_dict[(readable_upgrade, region)] = 1
    else:
        upgrade_dict[(readable_upgrade, region)] += 1


cal_nev_racers = 3128
new_england_racers = 1966
regions = ["British Columbia", "California/Nevada", "ECCC", "Europe", "Mid Atlantic", "Mountain West", "New England",
           "New York", "North Central", "Pacific Northwest", "South Central", "Southeast"]
regions_we_care_about = ["California/Nevada", "New England"]
categories = [5, 4, 3, 2, 1]
for region in regions_we_care_about:
    print region
    if region == "California/Nevada":
        total_racers = cal_nev_racers
    elif region == "New England":
        total_racers = new_england_racers
    to_4 = 0
    to_3 = 0
    to_2 = 0
    to_1 = 0
    if ((5, 4), region) in upgrade_dict:
        to_4 += upgrade_dict[((5,4), region)]
    if ((4, 3), region) in upgrade_dict:
        to_3 += upgrade_dict[((4, 3), region)]
    if ((5, 3), region) in upgrade_dict:
        to_3 += upgrade_dict[((5, 3), region)]
    if ((5, 2), region) in upgrade_dict:
        to_2 += upgrade_dict[((5, 2), region)]
    if ((4, 2), region) in upgrade_dict:
        to_2 += upgrade_dict[((4, 2), region)]
    if ((3, 2), region) in upgrade_dict:
        to_2 += upgrade_dict[((3, 2), region)]
    if ((5, 1), region) in upgrade_dict:
        to_1 += upgrade_dict[((5, 1), region)]
    if ((4, 1), region) in upgrade_dict:
        to_1 += upgrade_dict[((4, 1), region)]
    if ((3, 1), region) in upgrade_dict:
        to_1 += upgrade_dict[((3, 1), region)]
    if ((2, 1), region) in upgrade_dict:
        to_1 += upgrade_dict[((2, 1), region)]
    total_upgrades = to_4 + to_3 + to_2 + to_1
    print "Total racers in region: " + str(total_racers)
    print "Total racers receiving upgrade in region: " + str(total_upgrades)
    if to_4 != 0:
        print "Cat 4 upgrades per region racer: " + str(Decimal(to_4) / Decimal(total_racers))
        print "Percentage of upgrades to Cat 4: " + str(Decimal(to_4) / Decimal(total_upgrades))
    if to_3 != 0:
        print "Cat 3 upgrades per region racer: " + str(Decimal(to_3) / Decimal(total_racers))
        print "Percentage of upgrades to Cat 3: " + str(Decimal(to_3) / Decimal(total_upgrades))
    if to_2 != 0:
        print "Cat 2 upgrades per region racer: " + str(Decimal(to_2) / Decimal(total_racers))
        print "Percentage of upgrades to Cat 2: " + str(Decimal(to_2) / Decimal(total_upgrades))
    if to_1 != 0:
        print "Cat 1 upgrades per region racer: " + str(Decimal(to_1) / Decimal(total_racers))
        print "Percentage of upgrades to Cat 1: " + str(Decimal(to_1) / Decimal(total_upgrades))