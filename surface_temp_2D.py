import cdsapi

year = range(1979, 2022)

c = cdsapi.Client()

for i in year:
	c.retrieve(
	    'reanalysis-era5-single-levels',
	    {
	        'product_type': 'reanalysis',
	        'format': 'grib',
	        'variable': '2m_temperature',
	        'year': i,
	        'month': [
	            '01', '02', '03',
	            '04', '05', '06',
	            '07', '08', '09',
	            '10', '11', '12',
	        ],
	        'day': [
	            '01', '02', '03',
	            '04', '05', '06',
	            '07', '08', '09',
	            '10', '11', '12',
	            '13', '14', '15',
	            '16', '17', '18',
	            '19', '20', '21',
	            '22', '23', '24',
	            '25', '26', '27',
	            '28', '29', '30',
	            '31',
	        ],
	        'time': [
	            '00:00', '06:00', '12:00',
	            '18:00',
	        ],
	        'area': [
	            90, -180, -90,
	            180,
	        ],
			'grid': [
				'1.0', '1.0'
			],
	    },
	    't2m.' + str(i) + '.grib')
