import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap

st.set_page_config(
    page_title="KL Competitor Heatmap",
    page_icon="🧘🏻‍♀️",
    )

#creating a title for the app
st.title("Heatmap of KL's Yoga Market")

# Create a base map centered around Kuala Lumpur
m = folium.Map(location=[3.1390, 101.6869], zoom_start=11)

# Your list of latitudes and longitudes
data = {'The Flow Studio': [
    (3.1274188,101.6745625),
    (3.1519383363602462, 101.66553696882904),
    (3.138249, 101.63008),
    (3.052161, 101.671278)
    ],
    'karma yoga': [
        (3.1318964,101.6711135)
        ],
    'Life Hot Yoga': [
        (3.149766037831857, 101.59387235348427),
        (3.167091133373805, 101.65190068232039)
        ],
    'Celebrity Fitness': [
        (3.1301827,101.6710671),
        (3.1512698118957534, 101.6169901603),
        (3.0698452683269846, 101.69535177114773),
        (3.1193243119004923, 101.67848784897004),
        (3.1958333217962744, 101.63381297508522)
        ],
    'Urban Spring Pilates': [
        (3.1384434073561533, 101.6688006580661),
        (3.1682057077947823, 101.65239181115658)
        ],
    'AlignYoga': [
        (3.052142720526545, 101.67918610039212)
        ],
    'Surya Yoga': [
        (3.1212672,101.5954205),
        (3.078323903350539, 101.69372597375367),
        (3.0927007030010296, 101.68761344990328),
        (3.0448612,101.622157),
        (3.010448265835054, 101.53854430327854),
        (3.0978648832843207, 101.75346413257392),
        (3.017641745178442, 101.69612923218372)
        ],
    'Simplylife Yoga': [
        (3.179423396637816, 101.68323264272207)
        ],
    'YU+ Studio': [
        (3.0543866096330508, 101.67000526697564),
        (3.036385337758758, 101.76508320930336)
        ],
    'Omsphere': [
        (3.0531466874387894, 101.73909438046711)
        ],
    'Mysore Room': [
        (3.171403844928022, 101.66593865348423)
        ],
    'Sanctum Wellness at EQ': [
        (3.153035935376106, 101.7097521093033)
        ],
    'mYoga': [
        (3.1285862842180845, 101.71357731573829)
        ],
    'Art Printing Works Yoga': [
        (3.1244613625431485, 101.67427181573822)
        ],
    'Damai Studio and Cafe': [
        (3.1662218740184365, 101.71750229581187)
        ],
    'Life n Fitness': [
        (3.12873404090602, 101.63503775348423),
        (3.095408586930257, 101.73852216697564),
        (3.1408348512615536, 101.70754993813944)
        ],
    'Journey Within Studio': [
        (3.1550800734689615, 101.59488056882898)
        ],
    'Yogic Spandana': [
        (3.16200592618416, 101.74212885991994)
        ]
    }

regions = {'Bangsar': [
    (3.1274188,101.6745625),
    (3.1318964,101.6711135),
    (3.1301827,101.6710671),
    (3.1384434073561533, 101.6688006580661)
    ],
    'Kota Damansara': [
        (3.149766037831857, 101.59387235348427),
        (3.1212672,101.5954205),
        (3.1550800734689615, 101.59488056882898)],
    'Bukit Bintang': [
        (3.153035935376106, 101.7097521093033),
        (3.1285862842180845, 101.71357731573829),
        (3.1662218740184365, 101.71750229581187),
        (3.1408348512615536, 101.70754993813944),
        (3.16200592618416, 101.74212885991994)
        ],
    'Bukit Jalil': [
        (3.052161, 101.671278),
        (3.052142720526545, 101.67918610039212),
        (3.0543866096330508, 101.67000526697564)
        ],
    'Mont Kiara': [
        (3.1519383363602462, 101.66553696882904),
        (3.167091133373805, 101.65190068232039),
        (3.1682057077947823, 101.65239181115658),
        (3.171403844928022, 101.66593865348423)
        ],
    'Mid-Valley': [
        (3.1193243119004923, 101.67848784897004),
        (3.1244613625431485, 101.67427181573822)
        ],
    'Kepong Village': [
        (3.1958333217962744, 101.63381297508522)
        ],
    'Puchong Jaya': [
        (3.0448612,101.622157),
        ],
    'Kota Kemuning': [
        (3.010448265835054, 101.53854430327854)
        ],
    'Cheras': [
        (3.0978648832843207, 101.75346413257392),
        (3.0531466874387894, 101.73909438046711),
        (3.036385337758758, 101.76508320930336),
        (3.095408586930257, 101.73852216697564)
        ],
    'TTDI': [
        (3.138249, 101.63008),
        (3.1512698118957534, 101.6169901603),
        (3.12873404090602, 101.63503775348423),
        ],
    'Seri Kembangan': [
        (3.017641745178442, 101.69612923218372)
        ],
    'Sentul': [
        (3.179423396637816, 101.68323264272207)
        ],
    'Sri Petaling': [
        (3.0698452683269846, 101.69535177114773),
        (3.078323903350539, 101.69372597375367)
    ],
    'Kuchai': [
        (3.0927007030010296, 101.68761344990328)
    ]
    }

#Function to find the region of a studio
def find_region(lat, lon, regions):
    for region, coords in regions.items():
        if (lat, lon) in coords:
            return region
    return None

# Function to find all studios for a given latitude and longitude
def find_studios(lat, lon, data):
    matching_studios = []
    for studio, coords in data.items():
        if (lat, lon) in coords:
            matching_studios.append(studio)
    return matching_studios

# Function to format regions and studios in columns
def format_columns(regions_studios):
    # Create HTML table with no borders
    table_html = "<table style='width: 100%; border: 0;'><tr style='border: 0;'>"
    count = 0
    total_regions = len(regions_studios)
    remaining_regions = total_regions % 3

    for r, studios in regions_studios.items():
        if studios:  # Only consider regions with studios
            # Check if it's the last row and not a multiple of 3
            if count >= total_regions - remaining_regions and remaining_regions != 0:
                if remaining_regions == 1 and count % 3 == 0:  # If only one region, add padding on both sides
                    table_html += "<td style='border: 0;'></td>"
                elif remaining_regions == 2 and count % 3 == 0:  # If two regions, and it's the first one, just add it
                    pass
                elif remaining_regions == 2 and count % 3 == 1:  # If two regions, and it's the second one, add padding to the left first
                    table_html += "<td style='border: 0;'></td>"
            
            column_html = f"<td style='padding: 8px; width: 33%; border: 0; vertical-align: top;'><b>{r}:</b><br>"
            column_html += '<br>'.join(studios)
            column_html += "</td>"
            table_html += column_html
            
            count += 1

            if count % 3 == 0 and count != total_regions:
                table_html += "</tr><tr style='border: 0;'>"
            elif remaining_regions == 1 and count == total_regions:  # If only one region, add padding on the right after displaying it
                table_html += "<td style='border: 0;'></td>"
    
    table_html += "</tr></table>"
    return table_html

def create_streetview(lat,lon):
    return f"http://maps.google.com/maps?q=&layer=c&cbll={lat},{lon}&cbp=12,0,0,0,0)"


# Radio button for Studios vs. Regions
selection_type = st.radio("Select by:", ["Studios", "Regions"])

# Initialize a dictionary to store region-wise studio lists
region_studio_mapping = {region: [] for region in regions}

# Update the mapping based on data
for studio, coords in data.items():
    for coord in coords:
        region = find_region(coord[0], coord[1], regions)
        if region:
            region_studio_mapping[region].append(studio)

if selection_type == "Studios":
    # Implementing the "Select All" checkbox for studios
    select_all = st.checkbox("Select all Studios")
    if select_all:
        selections = list(data.keys())
    else:
        selections = st.multiselect("Which Yoga Studio do you want to see?", list(data.keys()))

    # Combine data from all selected studios into a single list and add markers with popups
    combined_data = []
    for s in selections:
        combined_data.extend(data[s])
        for point in data[s]:
            region = find_region(point[0], point[1], regions)
            streetview_url = create_streetview(point[0], point[1])
            popup_text = f"""
            <div style="width: 200px;">
                <b>{s}</b><br><br>
                <i>Region: {region}</i><br><br>
                <a href='{streetview_url}' target='_blank'>Open in Street View</a>
            </div>
            """
            folium.CircleMarker(
                location=point,
                radius=6,
                color="rgba(255, 255, 255, 0)",
                fill=True,
                fill_color="rgba(255, 255, 255, 0)",
                fill_opacity=0,
                popup=popup_text
            ).add_to(m)

else:
    # Implementing the "Select All" checkbox for regions
    select_all = st.checkbox("Select all Regions")
    if select_all:
        selections = list(regions.keys())
    else:
        selections = st.multiselect("Which Region do you want to see?", list(regions.keys()))

    # Combine data from all selected regions into a single list and add markers with popups
    combined_data = []
    for r in selections:
        combined_data.extend(regions[r])
        for point in regions[r]:
            studios = find_studios(point[0], point[1], data)
            studios_text = ', '.join(studios)
            streetview_url = create_streetview(point[0], point[1])
            popup_text = f"""
            <div style="width: 200px;">
                <b>{studios_text}</b><br><br>
                <i>Region: {r}</i><br><br>
                <a href='{streetview_url}' target='_blank'>Open in Street View</a>
            </div>
            """
            folium.CircleMarker(
                location=point,
                radius=6,
                color="rgba(255, 255, 255, 0)",
                fill=True,
                fill_color="rgba(255, 255, 255, 0)",
                fill_opacity=0,
                popup=popup_text
            ).add_to(m)



# Add a single heatmap to the base map using the combined data
HeatMap(combined_data).add_to(m)

# Save the map to an HTML file
st_folium(m,height=600,  width=700)

if selection_type == "Studios":
    regions_studios = {}
    for r, coords in regions.items():
        studios_in_region = [s for s in selections if s in region_studio_mapping[r]]
        if studios_in_region:
            regions_studios[r] = studios_in_region

    if regions_studios:
        st.write("**Selected Studios in Their Respective Region:**")
        st.markdown(format_columns(regions_studios), unsafe_allow_html=True)

else:
    regions_studios = {}
    for r in selections:
        studios_in_region = region_studio_mapping[r]
        if studios_in_region:
            regions_studios[r] = studios_in_region

    if regions_studios:
        st.write("**Studios in Selected Regions:**")
        st.markdown(format_columns(regions_studios), unsafe_allow_html=True)