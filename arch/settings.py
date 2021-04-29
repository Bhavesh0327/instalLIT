"""
This file contains the by-default values of the parameters
that should be passed to scrap data appropriately
"""


searching_criteria = { 
    'nd' : 'Name, Description', 
    'n' : 'Name Only', 
    'b' : 'Package Name',
    'N' : 'Exact Name',
    'k' : 'Keywords',
    'm' : 'Maintainer',
    'c' : 'Co-Maintainer',
    'M' : 'Maintainer, Co-Maintainer',
    's' : 'Submitter'     
}

sorting_criteria = {
    'n' : 'name',
    'v' : 'votes',
    'p' : 'popularity',
    'w' : 'voted',
    'o' : 'Notify',
    'm' : 'Maintainer',
    'l' : 'Last Modified'
}

sorting_order = {
    'a' : 'ascending',
    'd' : 'descending'
}

search_by = 'nd'

out_of_date = ''

sort_by = 'n'

sort_order = 'a'

per_page = 50
