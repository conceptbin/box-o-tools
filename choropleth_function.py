# Libraries
import geopandas
import contextily as ctx
import matplotlib.pyplot as plt

# Function for choropleth with 2 map layers on top of Contextily basemap
def makeChoroplethLDN(layer1, layer2, column_name):
    """Takes in two mapping layers as geodataframes: 
    layer1 should contain the choropleth data, 
    layer2 is for contextual information, 
    column_name: title of a column in layer1 with numerical data for the colour map.
    Output: 2-layer choropleth map on a dynamic basemap."""
    # Match the CRS for the two layers
    layer2 = layer2.to_crs(layer1.crs)
        
    # Range for choropleth
    vmin, vmax = 10, 700
    
    fig, ax = plt.subplots(figsize=(20, 20))
    
    #Set aspect to equal
    ax.set_aspect('equal')
    
    layer1.plot(ax=ax, column=column_name, cmap='Greens', linewidth=0.4, edgecolor='green', alpha=0.8, zorder=1)
    layer2.boundary.plot(ax=ax, color='blue', linewidth=0.4, alpha=0.8, zorder=2)
    
    # Add contextily basemap
    ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite, alpha=0.8)

    # Switch off axis markers
    ax.axis('off')
    
    # Create colourbar as legend
    sm = plt.cm.ScalarMappable(cmap='Greens', norm=plt.Normalize(vmin=vmin, vmax=vmax))
    sm._A = []
    cbar = fig.colorbar(sm)
    
    # Optional: Save to file before showing
    fig.savefig(r'output\choroplethLDN_2021-entry.png', dpi=300)
    
    m = plt.show()
    return(m)
