import urllib, urllib2

# https://developers.google.com/fusiontables/docs/v1/sql-reference#Select

API_KEY = "AIzaSyCDkUEzmWGBztutMePuSxMwYrgJkS2H_oA"

def rect_query(tableid, loc_col, minlat, minlng, maxlat, maxlng, select):
	sql = urllib.quote("SELECT {0} FROM {1} WHERE ST_INTERSECTS({2}, RECTANGLE(LATLNG({3}, {4}), LATLNG({5}, {6}))) limit 1".format(select, tableid, loc_col, minlat, minlng, maxlat, maxlng))
	url="https://www.googleapis.com/fusiontables/v1/query?sql={0}&key={1}".format(sql, API_KEY)
	print url
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	print response.read()
  
if __name__ == "__main__":
    #rect_query("0IInYZs4MzlZbZnVzaW9udGFibGVzOjEyNjU4NDc","'Location details'", "50.85", "-2.26", "51.76", "0.92", "*")
	rect_query("1I_LasxQCrP6FXNH8FjVnmhSrpdDrPfB-R61d2b8","'geometry'", "50.85", "-2.26", "51.76", "0.92", "geometry")
