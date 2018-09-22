library(som)
library(maptools)

0
training_data_name <- scan(
	"output_data/training_data_name_list.csv",
	sep=',',
	what="",
	quiet=TRUE
)
training_data_name

ngrams_matrix <- read.csv("output_data/ngrams_matrix.csv", header=F)
# ngrams_matrix <- read.csv("dummy.csv", header=F)
1
normalized_ngrams <- normalize(ngrams_matrix)
2
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=10, ydim=10, rlen=1) # 1min on 4,400 dim
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=20, ydim=20, rlen=500) # 40 min on 4,400 dim
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=30, ydim=30, rlen=1000) # 2.5 h on 4,400 dim
normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=30, ydim=30, rlen=300) # 
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=40, ydim=40, rlen=700) # ? h
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=50, ydim=50, rlen=100) # 3h on 4,400 dim
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=64, ydim=64, rlen=400)
# normalized_ngrams_dim_red <- som(normalized_ngrams, xdim=200, ydim=200, rlen=600)
3
normalized_ngrams_map <- normalized_ngrams_dim_red$visual[, 1:2]
4
# pdf("Rplots.pdf")
# plot(normalized_ngrams_map, xlim=c(-1,11), ylim=c(-1,11), pch=16)#, col="red")
# plot(normalized_ngrams_map, xlim=c(-5,25), ylim=c(-5,25), pch=16)#, col="red")
plot(normalized_ngrams_map, xlim=c(-5,35), ylim=c(-5,35), pch=16)#, col="red")
# plot(normalized_ngrams_map, xlim=c(-10,80), ylim=c(-10,80), pch=16)
# plot(normalized_ngrams_map, xlim=c(-10,210), ylim=c(-10,210), pch=16)
5
# text(normalized_ngrams_map$x, normalized_ngrams_map$y, labels=training_data_name)#, pos=1)#, col="blue")
pointLabel(normalized_ngrams_map$x, normalized_ngrams_map$y, labels=training_data_name, col="blue")#, pos=1)#, col="blue")
6
