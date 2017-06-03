'''
Created on 2 Jun 2017

@author: Lennon
'''
from reflection.proposal.AdministrationServices import ApprovalData

approvalDataJsonTemplate = "{{\"name\":\"{name}\",\"children\":[{list}]}}"

def approvalInfoToJsonString(approvalData):
    if (type(approvalData) is ApprovalData):
        parentDataList = ''
        if (len(approvalData.children) == 0):
            return approvalDataJsonTemplate.format(approvalData.name, '{"name": "None Found","size":1}')
        #For each child in the data
        for appData in approvalData.children:
            #Create a list of approval info
            infoList = ''
            for appInfo in appData.children:
                #For each child in the info concatenate to a list
                infoList = ',' + infoList + str(appInfo)
            #remove the last comma from the info list
            infoList = infoList.replace(',','',1)
            parentDataList = ',' + parentDataList + approvalDataJsonTemplate.format(name = appData.name, list = infoList)
            
        #Add to the parentDataList
        parentDataList = parentDataList.replace(',', '',1)
        #Generate an approval data template
        return approvalDataJsonTemplate.format(name = approvalData.name, list = parentDataList)
        
        
        
    else:
        raise Exception("Object must be of type ApprovalData")
        