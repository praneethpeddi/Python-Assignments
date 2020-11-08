import random
import operator


def generate_teams(n):
    team_list = []
    for i in range(1, n + 1):
        team_list.append('Team' + str(i))
    print(f"Total teams participating in the IPL : {team_list}")
    return team_list


def league_matches(teams):
    set_of_matches = []
    for i in range(len(teams)):
        for j in range(len(teams)):
            matches = (teams[i], teams[len(teams) - j - 1])
            if teams[i] != teams[len(teams) - j - 1]:
                set_of_matches.append(matches)
    print(f"Total set of league matches between each team : {set_of_matches}")
    print(f"Total number of league matches : {len(set_of_matches)}")
    return set_of_matches


def match_between_teams(teams, matches):
    total_score_each_team = {}
    for each_team in teams:
        total_score_each_team[each_team] = 0
    print(f"Total score of each team before league matches : {total_score_each_team}")
    for each_match in matches:
        res_each_match = random.choice(each_match)
        print(f"Winner of the team {each_match} : {res_each_match}")
        total_score_each_team[res_each_match] += 2
    print(f"Total score of each team after league matches : {total_score_each_team}")
    return total_score_each_team


def qualify_playoffs(total_score_each_team):
    playoff_teams = dict(sorted(total_score_each_team.items(), key=operator.itemgetter(1), reverse=True))
    print(f"Score of each team after sorting in descending order {playoff_teams}")
    for i in range(4):
        playoff_teams.popitem()
    print(f"Total number of teams qualified for playoffs : {playoff_teams}")
    return playoff_teams


def playoff_matches(playoff_teams):
    lis = [(k, v) for k, v in playoff_teams.items()]
    playoff1 = random.choice((lis[0][0], lis[1][0]))
    if playoff1 == (lis[0][0]):
        playoff1_looser = (lis[1][0])
    else:
        playoff1_looser = (lis[0][0])
    playoff2 = random.choice((lis[2][0], lis[3][0]))
    playoff3 = random.choice((playoff2, playoff1_looser))
    print(f"Team won in the playoff1, Finalist1 : {playoff1}")
    print(f"Team won in the playoff2 : {playoff2}")
    print(f"Team lost in the playoff1 : {playoff1_looser}")
    print(f"Team lost in the playoff3, Finalist2 : {playoff3}")
    return playoff1, playoff3


def final_match(finalist1, finalist2):
    winner = random.choice((finalist1, finalist2))
    return winner


def main():
    n = 8
    teams = generate_teams(n)
    matches = league_matches(teams)
    total_score_each_team = match_between_teams(teams, matches)
    playoff_teams = qualify_playoffs(total_score_each_team)
    finalist1, finalist2 = playoff_matches(playoff_teams)
    winner = final_match(finalist1, finalist2)
    print(f"Congratulations to the team {winner} for winning the league")


if __name__ == '__main__':
    main()
