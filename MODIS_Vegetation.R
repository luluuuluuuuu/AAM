library(MODISTools)

data(ConvertExample)
modis.subset <-
  ConvertToDD(XY = ConvertExample, LatColName = "lat", LongColName = "long")
modis.subset <- data.frame(lat = modis.subset[ ,1], long = modis.subset[ ,2])
modis.subset$start.date <- rep(2006, nrow(modis.subset))
modis.subset$end.date <- rep(2006, nrow(modis.subset))
GetProducts()
GetBands(Product = "MOD13Q1")
GetDates(Product = "MOD13Q1", Lat = modis.subset$lat[1], Long = modis.subset$long[1])

dir.create('./Vegetation')
setwd('./Vegetation')

MODISSubsets(LoadDat = modis.subset, Product = "MOD13Q1", Bands = "250m_16_days_NDVI",
             Size = c(1,1))
subset.string <- read.csv(list.files(pattern = ".asc")[1],
                          header = FALSE, as.is = TRUE)
