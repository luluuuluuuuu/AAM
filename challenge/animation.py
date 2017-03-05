import simplejson
from PyQt4.QtCore import *
from datetime import *

f=open('D:/challenge/animals.shp','r')

# create layer
vl = QgsVectorLayer("Point", "tweets", "memory")
vl.startEditing()
pr = vl.dataProvider()

# add fields
pr.addAttributes( [ QgsField("t", QVariant.String) ] )

# create features
for line in f:
        try:
                j=simplejson.loads(line)
                fet=QgsFeature()
                fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(j['geo']['coordinates'][1],j['geo']['coordinates'][0])))
                fet.setAttributeMap({0:QVariant(str(datetime.strptime(j['created_at'],'%a %b %d %H:%M:%S +0000 %Y')))})
                pr.addFeatures([fet])
        except:
                pass

vl.commitChanges()
vl.updateExtents()

QgsMapLayerRegistry.instance().addMapLayer(vl)
