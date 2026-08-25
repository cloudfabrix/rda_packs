This pack is designed for visualizing and analyzing infrastructure topology, providing comprehensive insights into asset relationships, dependencies, and physical locations. It leverages GraphDB to store and query topology data, offering multiple perspectives through the following views:

- **Topology View** (Hierarchical graph of infrastructure layers)
- **Path Visualization** (End-to-end connectivity tracing)
- **Geomap** (Geographic distribution of assets)
- **Nodes Report** (Tabular inventory of nodes and metadata)
- **Drilldown Topology** (Focused view of node relationships)


### Pre-requisite Steps 
- Add arango template from the resources folder to path: `Main Menu -> Configuration -> RDA Administration -> Object store -> Upload`. Give Name as `rda_arango_templates` and Folder name as `arango_templates`<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Topology%20Training/1.0.0/resources/arango_templates" target="_blank">Click here for Arango template</a><br>


### Quick Start Guide

| Step | Description |
|------|-------------|
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, Use `Launch Dashboard` menu option to navigate to the pack's dashboard. |
| 2    | Go to `Asset Navigator Topology` and open the `Dashboard` to view the `Topology`,`Node Details` and `Relations`. Navigate to `Documentation` for additional information.                                      |
| 3    | Go to `Topology View` and open the `Dashboard` to view the `Full Stack`,`Asset Map` and `Relationships`. Navigate to `Documentation` for additional information.                                                         |
| 4    | Go to `Customer Topology` and open the `Dashboard` and click on `Nodes` to view node specific details such as `Path Visualization`,`Topology`, and `Geomap`. Navigate to `Documentation` for additional information. |
| 5    | Go to `Data` to view the `Nodes` and `Edges` collection data from `topology_training_graph` GraphDB |