 CSP Map Coloring Problem

This project solves a Constraint Satisfaction Problem (CSP) using graph coloring techniques.

It includes:

Australia map coloring problem (5 regions, 3 colors)
Nairobi sub-county map coloring problem (17 regions, minimal colors)
 Objectives
Apply backtracking search algorithm
Ensure no two adjacent regions share the same color
Minimize number of colors used
Model real-world geography as a graph
 Algorithm Used

Backtracking Search (CSP Solver)

Constraint Checking:
Adjacent nodes cannot share the same color
Part A: Australia Map Coloring
Regions:
WA (Western Australia)
NT (Northern Territory)
SA (South Australia)
Q (Queensland)
NSW (New South Wales)
Colors:
Blue
Red
Green
Result:

Successfully colored using 3 colors while ensuring no adjacent regions share the same color.

🇰🇪 Part B: Nairobi Map Coloring
Sub-counties modeled as graph nodes:
Westlands
Kibra
Embakasi (various zones)
And other Nairobi sub-counties (total: 17 regions)
Colors used:
Blue
Red
Green
Yellow

Minimum number of colors depends on adjacency constraints in the graph.

 How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run Australia CSP
python australia_map_coloring.py
3. Run Nairobi CSP
python nairobi_map_coloring.py
 Output Example
WA -> Blue  
NT -> Red  
SA -> Green  
Q -> Blue  
NSW -> Red  
 Concepts Demonstrated
Constraint Satisfaction Problem (CSP)
Graph coloring
Backtracking algorithm
Real-world modeling of geography
 Author
IAN CEWA
