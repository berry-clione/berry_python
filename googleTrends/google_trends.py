import better_exceptions
import colorize
import colored_traceback.always

from pytrends.request import TrendReq
import pandas
import matplotlib.pyplot as plt

kw_list_en = ["AI"]
kw_list_jp = ["人工知能"]
png_line_graph_google_trend = "googleTrends.png"
output_csv_file_name = "googleTrends.csv"

class googleTrends:
	def get_google_trend_interest(kw_list, lang, geo_info):
		pytrends = TrendReq(hl=lang, tz=360)
		# pytrends = TrendReq(hl='ja-JP', tz=360)
		# pytrends = TrendReq(hl='en-US', tz=360)
		# pytrends.build_payload(
		# 	kw_list,
		# 	cat=0, # https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories
		# 	# timeframe='today 2-y',
		# 	timeframe='2018-01-01 2018-12-31',
		# 	geo='JP',
		# 	gprop=''
		# )
		# print(pytrends.related_queries())
		# print(pytrends.related_topics())
		
		df_trends = pytrends.get_historical_interest(
			kw_list,
			year_start=2009,
			month_start=4,
			day_start=1,
			hour_start=0,
			year_end=2019,
			month_end=3,
			day_end=31,
			hour_end=0,
			cat=0,
			geo=geo_info,
			# geo='JP',
			# geo='US',
			gprop='',
			sleep=0
		)
		df_trends = df_trends.set_index([df_trends.index.date, df_trends.index])
		df_trends.index.names = ['date', 'index']
		df_trends = df_trends.sum(level=['date'])
		df_trends = df_trends.drop("isPartial", axis=1)
		# df_trends.columns = ["".join(["Google:", word]) for word in kw_list]
		df_trends.columns = kw_list
		print(df_trends.columns.tolist())
		return df_trends

	def output_csv_google_trend(df_trends, output_csv_file_name):
		df_trends.to_csv(output_csv_file_name)

	def output_line_graph_google_trend(df_trends, png_line_graph_google_trend):
		plt.rcParams['font.family'] = 'AppleGothic'
		plt.figure()
		df_trends.plot(figsize=(9, 3), lw=.5)
		# plt.show()
		plt.savefig(png_line_graph_google_trend)
		plt.close('all')

	def concat_fillna_dataframe(dataframe_list):
		# dataframe_list = [df_001, df_002, ...]
		df_concat = pandas.concat(dataframe_list, axis=1)
		df_concat = df_concat.fillna(0)
		return df_concat

####################

# df_trends_wd = googleTrends.get_google_trend_interest(kw_list_en, lang='', geo_info='')
df_trends_en = googleTrends.get_google_trend_interest(kw_list_en, lang='en-US', geo_info='US')
df_trends_jp = googleTrends.get_google_trend_interest(kw_list_jp, lang='ja-JP', geo_info='JP')

df_concat = googleTrends.concat_fillna_dataframe([df_trends_en, df_trends_jp])

googleTrends.output_csv_google_trend(df_concat, output_csv_file_name)

googleTrends.output_line_graph_google_trend(df_concat, png_line_graph_google_trend)


