"""
The Number of Representatives shall not exceed one for every thirty Thousand,
but each State shall have at Least one Representative…”
—	U.S. Constitution, Article I, section 2, clause 3

States should, in theory, have a number of representatives proportional
to their populations. In an effort to not have thousands of representatives,
the original rules were adjusted. Let's see what that has done to the
population : votes ratio.
"""

from credentials import *
import pandas as pd
import quandl


def importRepNumbers():
    line = 'https://www.britannica.com/topic/United-States-House-of-' \
           'Representatives-Seats-by-State-1787120'

    reps = pd.read_html(line)
    df = reps[0]



    # dropping total row and NaN row from table
    # It looks like pandas uses a linked list in the backend, drop 51 then 52
    # fails. Drop 51 twice works, but that seems more messy than this way
    df.drop(df.index[52], inplace=True)
    df.drop(df.index[51], inplace=True)

    # drops 0 representatives line
    df.drop(df.index[0], inplace=True)

    df.columns = ["State", "Reps"]
    df.set_index("State", inplace=True)
    return df

def importPopulation():
    line = 'http://www.nationsonline.org/oneworld/US-states-population.htm'

    population = pd.read_html(line)
    pop = population[2][3][1:]
    state = population[2][2][1:]

    df = pd.DataFrame(
        {
            'Population':pop,
            "State":state
        }
    )

    df.set_index("State", inplace=True)
    return df


reps = importRepNumbers()
population = importPopulation()

joined = reps.join(population)
print(joined)