'''
Created on 2 Jun 2017

@author: Lennon
'''
from reflection.proposal.AdministrationServices import ProjectDataStructure

approvalDataJsonTemplate = "{{\"name\":\"{name}\",\"children\":[{list}],\"detail\":\"{detail}\",\"id\":\"{id}\",\"select\":\"{select}\"}}"
emptyDataStub = '{"name": "None Found","size":1}'

def approvalInfoToJsonString(approvalData):
    if (type(approvalData) is ProjectDataStructure):
        parentDataList = ''
        if (len(approvalData.children) == 0):
            return approvalDataJsonTemplate.format(name = approvalData.name, list = emptyDataStub, detail = approvalData.information, id = approvalData.dbId, select = approvalData.clickable)
        #For each child in the data
        for appData in approvalData.children:
            #Create a list of approval info
            if (len(appData.children) == 0):
                infoList = emptyDataStub
            else:
                infoList = ",".join(str(appInfo) for appInfo in appData.children)
            #remove the last comma from the info list
            parentDataList = ',' + parentDataList + approvalDataJsonTemplate.format(name = appData.name, list = infoList, detail = appData.information, id = appData.dbId, select = appData.clickable)
            
        #Add to the parentDataList
        parentDataList = parentDataList.replace(',', '',1)
        #Generate an approval data template
        return approvalDataJsonTemplate.format(name = approvalData.name, list = parentDataList, detail = approvalData.information, id = approvalData.dbId, select = approvalData.clickable)
        
    else:
        raise Exception("Object must be of type ProjectDataStructure")
        