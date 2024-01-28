# Author- Zach Charlick - Adapted from Jerome Briot
# EDIT LINE 96 TO THE FULL PATH OF THE FILE SAVE LOCATION

import adsk.core, traceback
import os

def populateDict(obj):

    tlObj = []

    for t in obj:
        try:
            index = t.index
        except:
            index = 99999
        try:
            name = t.name
        except:
            name = ''
        try:
            entity = t.entity.objectType
        except:
            entity = ''
        try:
            healthState = t.healthState
        except:
            healthState = -1
        try:
            errorOrWarningMessage = t.errorOrWarningMessage
        except:
            errorOrWarningMessage = ''
        try:
            component = t.entity.parentComponent.name
        except:
            component = ''

        tlObj.append({
                    'index': index,
                    'name': name,
                    'entity': entity,
                    'healthState': healthState,
                    'errorOrWarningMessage': errorOrWarningMessage,
                    'component': component
                    })

    return tlObj


def populateStr(tlObj):

    msg = ''
    for t in tlObj:
        #msg += '{:05d}, {}, {}, {}, {}, {}\n'.format(t['index'], t['name'], t['entity'], t['component'], t['healthState'], t['errorOrWarningMessage'])
        msg += '{:05d}, {}, {}, {}\n'.format(t['index'], t['name'], t['entity'], t['component'])

        for param in allParam:
            if param.createdBy.name == t['name']:
                msg += '{}, {}, {}\n'.format(param.createdBy.name, param.name, param.expression)

    return msg


def saveToCSV(msg, filename):

    f = open(filename, 'w')
    f.write(msg)
    f.close()


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct

        global allParam
        allParam = product.allParameters

        tl = product.timeline

        if tl.count==0:
            ui.messageBox('The timeline is empty')
            return

        grp = []
        for t in tl:
            if t.isGroup:
                grp.append(t)

        tlObj = populateDict(tl)

        msg = populateStr(tlObj)

        # CHANGE THIS TO THE FULL PATH OF DESIRED .CSV LOCATION
        csv_path = "C:\\Users\\zacha\\Desktop\\"

        filename = os.path.expanduser(csv_path + app.activeDocument.dataFile.name + "_complete_history.csv")
        saveToCSV(msg, filename)

        for g in grp:
            tlObj = populateDict(g)
            msg = populateStr(tlObj)
            filename = os.path.expanduser(csv_path + app.activeDocument.dataFile.name + "_grp_" + g.name + ".csv")
            saveToCSV(msg, filename)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))