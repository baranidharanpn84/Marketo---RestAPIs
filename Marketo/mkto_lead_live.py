from marketorestpython.client import MarketoClient
import csv, os, pandas, numpy

export_file = 'C:/Talend/JobFiles/Marketo/Export/Lead/file_mkto_lead_live.csv' # Put a path as per your  directory. New file created and will have email, ID, status columns
batch_size = 300

# SPECIFY CLIENT CREDENTIALS
munchkin_id =""
client_id = ""
client_secret = ""

mc = MarketoClient(munchkin_id, client_id, client_secret)

if __name__ == "__main__":
    a = 0
    b = 0
    for leads in mc.execute(method='get_multiple_leads_by_list_id_yield', listId=76414, fields=[
        'id',
        'firstName',
        'middleName',
        'lastName',
        'email',
        'company',
        'site',
        'street',
        'city',
        'state',
        'country',
        'postalCode',
        'website',
        'mainPhone',
        'annualRevenue',
        'numberOfEmployees',
        'industry',
        'sicCode',
        'mktoCompanyNotes',
        'sfdcAccountId',
        'mktoName',
        'personType',
        'mktoIsPartner',
        'isLead',
        'mktoIsCustomer',
        'isAnonymous',
        'salutation',
        'phone',
        'mobilePhone',
        'fax',
        'title',
        'contactCompany',
        'dateOfBirth',
        'personPrimaryLeadInterest',
        'originalSourceType',
        'originalSourceInfo',
        'registrationSourceType',
        'registrationSourceInfo',
        'originalSearchEngine',
        'originalSearchPhrase',
        'originalReferrer',
        'emailInvalid',
        'emailInvalidCause',
        'unsubscribed',
        'unsubscribedReason',
        'doNotCall',
        'mktoDoNotCallCause',
        'doNotCallReason',
        'mktoPersonNotes',
        'sfdcType',
        'sfdcContactId',
        'anonymousIP',
        'inferredCompany',
        'inferredCountry',
        'inferredCity',
        'inferredStateRegion',
        'inferredPostalCode',
        'inferredMetropolitanArea',
        'inferredPhoneAreaCode',
        'createdAt',
        'updatedAt',
        'leadPerson',
        'leadRole',
        'leadSource',
        'leadStatus',
        'leadScore',
        'urgency',
        'priority',
        'relativeScore',
        'relativeUrgency',
        'rating',
        'sfdcLeadId',
        'sfdcLeadOwnerId',
        'leadPartitionId',
        'leadRevenueCycleModelId',
        'leadRevenueStageId',
        'Interest_DI',
        'Interest_DQ',
        'Interest_MDM',
        'Interest_ESB',
        'Sugar_lead_id',
        'Sugar_cid',
        'Business_zone',
        'Phone_office_valid',
        'Phone_mobile_valid',
        'Language_preference',
        'Phone_extension',
        'Department',
        'Status_in_CRM',
        'BDR_interest_determination',
        'Bounced_elsewhere',
        'Account_potential',
        'acquisitionProgramId',
        'mktoAcquisitionDate',
        'Test',
        'LastScoring-Adoption',
        'jigsawContactStatus',
        'jigsawContactId',
        'sfdcId',
        'Interest_TIF',
        'Interest_TFS',
        'LastInteractionDate',
        'JobFunction',
        'PrimaryProductInterest',
        'LeadComments',
        'SalesAlert',
        'Alert',
        'Third-PartySource',
        'Marketo_SFDC_Id',
        'NetSuiteId',
        'SendtoNetsuite',
        'Push_to_Sales',
        'NS_Email',
        'AccountType',
        'Territory',
        'Job_Level',
        'Use_Case',
        'Last_Scoring_UserDoc',
        'Last_Scoring_ProductReg',
        'Last_Scoring_Tutorial',
        'Adoption_Level',
        'jigsawCompanyStatus',
        'jigsawCompanyId',
        'Nurture_Campaign_Assigned',
        'Alert_Date',
        'Lead_Comment_History',
        'Indicated_Industry',
        'SD_Company_Name',
        'SD_Company_Address',
        'SD_Company_State',
        'SD_Company_Postal_Code',
        'SD_Company_Country',
        'SD_Company_Phone',
        'SD_Source',
        'SD_ID',
        'SD_Date',
        'SD_Match_Confidence',
        'SD_Company_Fax',
        'SD_Entity_Type',
        'SD_Business_Description',
        'SD_Ultimate_Parent_ID',
        'SD_Ultimate_Parent_Name',
        'NAIC_Code',
        'SD_Revenue_Currency',
        'SD_Assets_USD',
        'SD_Company_Stock_Exchange',
        'SD_Company_Ticker_Symbol',
        'SD_Number_Employees',
        'ProductVersion',
        'Telemarketing_Status',
        'Interest_BPM',
        'Interest_BigData',
        'Phone_Invalid',
        'PostalCode_Invalid',
        'EmailInvalid_API',
        'CurrentNurtureProgram',
        'Asset',
        'Username',
        'LeadSelf-Identifier',
        'RoadshowChoice1',
        'RoadshowChoice2',
        'Asset_History',
        'gender',
        'facebookDisplayName',
        'twitterDisplayName',
        'linkedInDisplayName',
        'facebookProfileURL',
        'twitterProfileURL',
        'linkedInProfileURL',
        'facebookPhotoURL',
        'twitterPhotoURL',
        'linkedInPhotoURL',
        'facebookReach',
        'twitterReach',
        'linkedInReach',
        'facebookReferredVisits',
        'twitterReferredVisits',
        'linkedInReferredVisits',
        'totalReferredVisits',
        'facebookReferredEnrollments',
        'twitterReferredEnrollments',
        'linkedInReferredEnrollments',
        'totalReferredEnrollments',
        'lastReferredVisit',
        'lastReferredEnrollment',
        #'TalendEmployee',
        'TimeSlot',
        'TimeSlot2',
        'syndicationId',
        'CampaignSource',
        'CampaignMedium',
        'CampaignTerm',
        'CampaignID',
        'Registered_BD',
        'Registered_ESB',
        'Registered_MDM',
        'Registered_DQ',
        'Registered_DI',
        'CampaignContent',
        'RegisteredProductName',
        'ProductNameRecognized',
        'RegisteredProducts',
        'RegisteredProductType',
        'ForumNotes',
        'RoadshowChoice3',
        'QualifiedUser',
        'LeadSourceDetail',
        'upgradeinterest',
        'facebookId',
        'twitterId',
        'linkedInId',
        'Rep_First_Name',
        'Rep_Last_Name',
        'Rep_Email_Address',
        'Rep_Job_Title',
        'Behavior_Score',
        'Demographic_Score',
        'Product_Evaluation_Request',
        'Product_Evaluation_Request_History',
        'Last_Product_Evaluation_Request_Date',
        'Product_Evaluation_Request_Activity_Log',
        'TechTarget_AI_Contact_Link',
        'Nurture_Program_Changed',
        'Named_Account',
        'Rep_Phone_Number',
        'nurture_campaign_flow_stop',
        'nurture_campaign_flow_start',
        'sandboxInstance',
        'cookies',
        'CurrencyIsoCode',
        'EmailBouncedReason',
        'EmailBouncedDate',
        'DSCORGPKG__DeletedFromDiscoverOrg__c',
        'DSCORGPKG__DiscoverOrg_Company_ID__c',
        'DSCORGPKG__DiscoverOrg_ID__c',
        'DSCORGPKG__DiscoverOrg_Technologies__c',
        'DSCORGPKG__ITOrgChart__c',
        'DSCORGPKG__LinkedIn_URL__c',
        'DSCORGPKG__ReportsTo__c',
        'DSCORGPKG__Twitter_URL__c',
        'Alert_Phone__c',
        'Competition__c',
        'Do_Not_Call_Reason__c',
        'Function_called_Job_Function_in_Marketo__c',
        'Job_Role__c',
        'LinkedIn_URL__c',
        'MQL_Channel__c',
        'MQL_Date__c',
        'MQL_Program__c',
        'Mobile_Phone__c',
        'Notes_for_Marketing_Only__c',
        'Nurture_Return__c',
        'Other_Competition__c',
        'Phone_Business__c',
        'Phone_Extension_Business__c',
        'Reason_Code__c',
        'RegionF__c',
        'Region__c',
        'mkto_si__HideDate__c',
        'mkto_si__MSIContactId__c',
        'CurrencyIsoCode_account',
        'Channel_tier__c_account',
        'Customer_Type__c',
        'Region__c_account',
        'DSCORGPKG__DiscoverOrg_ID__c_account',
        'Account_Potential__c_account',
        'Account_Subsidiary__c',
        'Competition__c_account',
        'Language__c',
        'Other_Competition__c_account',
        'CurrencyIsoCode_contact',
        'Alt_Email__c',
        'Function__c',
        'Use_Case__c_contact',
        'mkto_si__Sales_Insight__c',
        'lastProgramChannel',
        'lastProgram',
        'acquisitionChannel',
        'Eval_EULA',
        'recycled_date',
        'pushtoNetSuite',
        'Country__c',
        'Lead_Lifecyle__c',
        'MQL_Program_X__c',
        'Sales_Activities_MQL__c',
        'Sourced_Industry__c',
        'Sourced_Phone__c',
        'State__c',
        'Subsidiary_Auto__c',
        'Territory__c',
        'RecordTypeId',
        'Oppstageflag__c',
        'Contact_Status__c',
        'Converted_Department__c',
        'MQL_Offer_Name',
        #'Channel_Offer',
        'Marketo_Lead_ID',
        'mktomerge',
        'External_Id__c',
        'Subsidiary__c_contact',
        'Salesforce_Internal_Id__c',
        'Date_of_First_Sale__c',
        'Push_To_NetSuite_Reason__c',
        'Contact_Us_Reason__c',
        'VAT_ID__c',
        'NS_Account_Owner__c',
        'Parent_Acct__c',
        'SF_Customer_Number__c',
        'Customer_Health__c',
        'Customer_Tier__c',
        'Territory_Focus__c',
        'Country_Group__c',
        'Account_Currency_Formula__c',
        'User_Subsidiary__c',
        'CSM_Customer_Description__c',
        'Health_Reason__c',
        'Salesforce_Internal_Id_del__c',
        'RecordTypeId_lead',
        'Job_Function__c',
        'Domain_group__c',
        'Country__c_account',
        'Owner_NetSuite_Id__c',
        'Outdated_Region__c',
        'Hours_Since_MQL__c',
        'companySFDC',
        'lastNameSFDC',
        'Opportunity__c',
        'cSMFullName',
        'Lead_Qualification_Date__c',
        'download_status',
        'Company_HQ_Location_State_Province__c',
        'Channel__c',
        'Channel_Partner__c',
        'Account_Description__c',
        'Account_Tier__c',
        'Health_Score__c',
        'Health_Required_Actions__c',
        'Health_Action_Ownership__c',
        'Health_Action_Status__c',
        'Renewal_Risk__c',
        'Renewal_Risk_Comment__c',
        'Upsell_Risk__c',
        'Upsell_Risk_Comment__c',
        'Customer_Sat_Risk__c',
        'Customer_Sat_Risk_Comment__c',
        'Competitive_Threat_Risk__c',
        'Competitive_Threat_Risk_Comment__c',
        'Strategic_Relationship_Risk__c',
        'Strategic_Relationship_Risk_Comment__c',
        'Adoption_Risk__c',
        'Adoption_Risk_Comment__c',
        'Proven_Value_Risk__c',
        'Proven_Value_Risk_Comment__c',
        'Other_Risk__c',
        'Other_Risk_Comment__c',
        'Deployment_Progress__c',
        'Laster_QBR__c',
        'Next_QBR__c',
        'Assigned_CSM__c',
        'LID__LinkedIn_Company_Id__c',
        'LID__LinkedIn_Member_Token__c',
        'LID__LinkedIn_Company_Id__c_account',
        'qbdialer__Dials__c',
        'qbdialer__LastCallTime__c',
        'qbdialer__ResponseTime__c',
        'qbdialer__Dials__c_account',
        'qbdialer__LastCallTime__c_account',
        'qbdialer__ResponseTime__c_account',
        'UniqueEntry__Contact_Dupes_Ignored__c',
        'UniqueEntry__Lead_Dupes_Ignored__c',
        'UniqueEntry__Account_Dupes_Ignored__c',
        'preMQLProgramAttribution',
        'mQLProgramAttribution',
        'sQLProgramAttribution',
        'sALProgramAttribution',
        'winProgramAttribution',
        'Days_Since_MQLs__c',
        'Days_Since_MQLs_del__c',
        'interestTIC',
        'TIC_Credentials_Issue_Date__c',
        'NanoCloud_Account_Created_Date__c',
        'of_calls_per_lead__c',
        'companySFDCClone',
        'lastNameSFDCClone',
        'acquisition_Channel_temp',
        'updatedFromAPI',
        'RingLead_Status',
        'mKTOdummyfield',
        'MQL_Program_temp',
        'revenueCycleDatesKnown',
        'revenueCycleDatesEngaged',
        'revenueCycleDatesMQL',
        'revenueCycleDatesASDRAccepted',
        'revenueCycleDatesSQL',
        'revenueCycleDatesPipeline',
        'revenueCycleDatesBestCase',
        'revenueCycleDatesCommit',
        'revenueCycleDatesCustomer',
        'revenueCycleDatesRenewal',
        'revenueCycleDatesUpsell',
        'revenueCycleDatesExpired',
        'revenueCycleDatesInactive',
        'revenueCycleDatesBadData',
        'revenueCycleDatesUnqualified',
        'revenueCycleDatesRecycled',
        'revenueCycleDatesReturntoADR',
        'revenueCycleDatesLost',
        'revenueCycleCurrentStage',
        'SD_Lead_Notes__c',
        'SD_Company_Address__c',
        'SD_Company_City__c',
        'SD_Business_Description__c',
        'SD_Company_Country__c',
        'SD_IT_Budget__c',
        'SD_IT_Employees__c',
        'SD_Company_Postal_Code__c',
        'SD_Tech_Business_Intelligence__c',
        'SD_Tech_CRM_MarketingAutomation__c',
        'SD_Tech_DataManagement__c',
        'SD_Tech_Data_Storage__c',
        'SD_Tech_Databases__c',
        'SD_Tech_ERP_HR_HCM_FI__c',
        'SD_Tech_Enterprise_Applications__c',
        'SD_Tech_Hardware_OS_SystemsEnvironment__c',
        'SD_Tech_ITSM__c',
        'SD_Tech_Languages__c',
        'SD_Tech_Programming_Tools__c',
        'SD_Company_Address__c_contact',
        'SD_Company_City__c_contact',
        'SD_Company_Postal_Code__c_contact',
        'Phone_1st_3_Digits__c',
        'Sales_Activities_MQL_Dials__c',
        'i__CreatedForUser__c',
        'i__DaysSinceLastMail__c',
        'i__LastInboundMail__c',
        'i__LastInboundSent__c',
        'i__LastInboundTime__c',
        'i__LastMailSent__c',
        'i__LastMailTimeDelta__c',
        'i__LastMailTime__c',
        'i__LastMail__c',
        'i__LastOutboundMail__c',
        'i__LastOutboundSent__c',
        'i__LastOutboundTime__c',
        'i__OtherEmails__c',
        'i__DaysSinceLastMail__c_account',
        'i__LastInboundMail__c_account',
        'i__LastInboundSent__c_account',
        'i__LastInboundTime__c_account',
        'i__LastMailSent__c_account',
        'i__LastMailTimeDelta__c_account',
        'i__LastMailTime__c_account',
        'i__LastMail__c_account',
        'i__LastOutboundMail__c_account',
        'i__LastOutboundSent__c_account',
        'i__LastOutboundTime__c_account',
        'mktotempfield',
        'sDITBudgetC',
        'sDITEmployeesC',
        'sDTechBusinessIntelligenceC',
        'sDTechCRMMarketingAutomationC',
        'sDTechDataManagementC',
        'sDTechDataStorageC',
        'sDTechDatabasesC',
        'sDTechERPHRHCMFIC',
        'sDTechEnterpriseApplicationsC',
        'sDTechHardwareOSSystemsEnvironmentC',
        'sDTechITSMC',
        'sDTechLanguagesC',
        'sDTechProgrammingToolsC',
        'sDBusinessDescriptionC',
        'sDCompanyCountryC',
        'mostRecentLeadSource',
        'mostRecentLeadSourceDetail',
        'Product_Solution_Integration_Cloud__c',
        'updateFromDiscoverOrg',
        'qbdialer__CloseDate__c',
        'qbdialer__CloseScore__c',
        'qbdialer__ContactDate__c',
        'qbdialer__ContactScoreId__c',
        'qbdialer__ContactScore__c',
        'qbdialer__TimeZoneSidKey__c',
        'qbdialer__TimeZoneSidKey__c_account',
        'NPS_Contact__c',
        'Executive_Sponsor__c',
        'Gainsight_Health__c',
        'Renewal_Status__c',
        'Renewal_Type__c',
        'externalCompanyId',
        'sf_leadid__c',
        'sf_contactid__c',
        'Mass_Update_for_Marketo__c',
        'DSCORGPKG__DiscoverOrg_Created_On__c',
        'DSCORGPKG__External_DiscoverOrg_Id__c',
        'DSCORGPKG__department__c',
        'DSCORGPKG__DiscoverOrg_Created_On__c_account',
        'DSCORGPKG__External_DiscoverOrg_Id__c_account',
        'Renew_Loss__c',
        'Customer_Categorization__c',
        'reasonsNotPromoted',
        'CAB_Member__c',
        'White_Glove__c',
        'X1_How_is_the_customer_measuring_success__c',
        'X2_Are_they_we_achieving_that_success__c',
        'X3_How_has_their_experience_been__c',
        'externalSalesPersonId',
        'End_User_ACV__c',
        'End_User_TCV__c',
        'Partner_ACV__c',
        'Partner_TCV__c',
        'Reseller_ACV__c',
        'Reseller_TCV__c',
        'aWSUsage',
        'aWSInfoShare',
        'qbdialer__CloseDate__c_account',
        'qbdialer__CloseScore__c_account',
        'CSM_Email_Address__c',
        'CSM_Phone_Number__c',
        'Account_Channel_Tier__c',
        'landing_page_language',
        'Assigned_CSA__c',
        'Buyer_Journey_Stage__c',
        'AVA__AVAAI_date_added__c',
        'AVA__AVAAI_first_message_date__c',
        'AVA__AVAAI_hot_lead__c',
        'AVA__AVAAI_hot_lead_date__c',
        'AVA__AVAAI_last_message_date__c',
        'AVA__AVAAI_last_response_date__c',
        'AVA__AVAAI_lead_at_risk__c',
        'AVA__AVAAI_lead_at_risk_date__c',
        'AVA__AVAAI_options__c',
        'AVA__AVAAI_score__c',
        'AVA__AVAAI_status__c',
        'AVA__Campaign__c',
        'IsPartner',
        'IsCustomerPortal',
        'Account_OTRS_ID__c',
        'Total_Active_User_Support_Licenses__c',
        'Total_Portal_Support_Users__c',
        'Customer_Preferred_Region__c',
        'Active_Support_User__c',
        'License_Company_Name__c',
        'License_End_Date__c',
        'License_Start_Date__c',
        'Primary_Support_Contact__c',
        'Tier__c',
        'Support_Contact__c',
        'customer_id__c',
        'License_Service_Level__c',
        'account_code',
        'Executive_Contact__c',
        'Champion_Contact__c',
        'Billing_Contact__c',
        'Reference_Contact__c',
        'Architect_Contact__c',
        'Total_Opportunities__c',
        'Total_Open_Opportunities__c',
        'Super_Contact_User__c',
        'Conversica_Outreach_Context__c',
        'Conversica_Inquiry_Verb__c',
        'Conversica_Outreach_Title__c',
        'CSM_Brief_Company_Overview__c',
        'CSM_Brief_Background_on_Account__c',
        'CSM_Business_Case_Why_Talend__c',
        'CSM_Competitive_Landscape__c',
        'A_Initial_Adoption_Usage__c',
        'A_Initial_Business_Case__c',
        'A_Initial_Success_Criteria__c',
        'A_Initial_Use_Case__c',
        'D_Initial_Adoption_Usage__c',
        'D_Initial_Business_Case__c',
        'D_Initial_Success_Criteria__c',
        'D_Initial_Use_Case__c',
        'E_Initial_Deployment__c',
        'M_Initial_Business_Case_Location__c',
        'M_Initial_Success_Criteria_Location__c',
        'M_Initial_Use_Case_Location__c',
        'MAE_Presentation_URL__c',
        'MAE_Record_Session_URL__c',
        'Web_User_Login__c',
        'LeadsProfiler__Business_Group__c',
        'LeadsProfiler__Business_Group_ref__c',
        'LeadsProfiler__Buyer_Persona__c',
        'LeadsProfiler__Buyer_Persona_ref__c',
        'LeadsProfiler__ChangeRankReason__c',
        'LeadsProfiler__City__c',
        'LeadsProfiler__City_ref__c',
        'LeadsProfiler__Company_Profile__c',
        'LeadsProfiler__Company_Profile_ref__c',
        'LeadsProfiler__Company_Revenue__c',
        'LeadsProfiler__Company_Revenue_ref__c',
        'LeadsProfiler__Company_Size__c',
        'LeadsProfiler__Company_Size_ref__c',
        'LeadsProfiler__Country__c',
        'LeadsProfiler__Country_ref__c',
        'LeadsProfiler__DataObject__c',
        'LeadsProfiler__OriginalRank__c',
        'LeadsProfiler__OriginalRank_ref__c',
        'LeadsProfiler__Probability_Delta__c',
        'LeadsProfiler__Probability_Delta_ref__c',
        'LeadsProfiler__SalesPredict_Last_Update__c',
        'LeadsProfiler__SalesPredict_Last_Update_ref__c',
        'LeadsProfiler__SalesPredict_Rank__c',
        'LeadsProfiler__SalesPredict_report_rank__c',
        'LeadsProfiler__SalesPredict_report_rank_ref__c',
        'LeadsProfiler__Score__c',
        'LeadsProfiler__Score_ref__c',
        'LeadsProfiler__Solution_Fit__c',
        'LeadsProfiler__Solution_Fit_ref__c',
        'LeadsProfiler__State__c',
        'LeadsProfiler__State_ref__c',
        'LeadsProfiler__Street__c',
        'LeadsProfiler__Street_ref__c',
        'LeadsProfiler__Title__c',
        'LeadsProfiler__Title_ref__c',
        'LeadsProfiler__Vertical__c',
        'LeadsProfiler__Vertical_ref__c',
        'LeadsProfiler__Business_Group__c_account',
        'LeadsProfiler__Business_Group_ref__c_account',
        'LeadsProfiler__Buyer_Persona__c_account',
        'LeadsProfiler__Buyer_Persona_ref__c_account',
        'LeadsProfiler__ChangeRankReason__c_account',
        'LeadsProfiler__City__c_account',
        'LeadsProfiler__City_ref__c_account',
        'LeadsProfiler__Company_Profile__c_account',
        'LeadsProfiler__Company_Profile_ref__c_account',
        'LeadsProfiler__Company_Revenue__c_account',
        'LeadsProfiler__Company_Revenue_ref__c_account',
        'LeadsProfiler__Company_Size__c_account',
        'LeadsProfiler__Company_Size_ref__c_account',
        'LeadsProfiler__Country__c_account',
        'LeadsProfiler__Country_ref__c_account',
        'LeadsProfiler__DataObject__c_account',
        'LeadsProfiler__OriginalRank__c_account',
        'LeadsProfiler__OriginalRank_ref__c_account',
        'LeadsProfiler__Probability_Delta__c_account',
        'LeadsProfiler__Probability_Delta_ref__c_account',
        'LeadsProfiler__Renewal_Probability_Delta__c',
        'LeadsProfiler__Renewal_Probability_Delta_ref__c',
        'LeadsProfiler__Renewal_Score__c',
        'LeadsProfiler__Renewal_Score_ref__c',
        'LeadsProfiler__SalesPredict_Renewal_Rank__c',
        'LeadsProfiler__SalesPredict_Renewal_report_rank__c',
        'LeadsProfiler__SalesPredict_Renewal_report_rank_ref__c',
        'LeadsProfiler__SalesPredict_rank__c_account',
        'LeadsProfiler__SalesPredict_report_rank__c_account',
        'LeadsProfiler__SalesPredict_report_rank_ref__c_account',
        'LeadsProfiler__Score__c_account',
        'LeadsProfiler__Score_ref__c_account',
        'LeadsProfiler__Solution_Fit__c_account',
        'LeadsProfiler__Solution_Fit_ref__c_account',
        'LeadsProfiler__State__c_account',
        'LeadsProfiler__State_ref__c_account',
        'LeadsProfiler__Street__c_account',
        'LeadsProfiler__Street_ref__c_account',
        'LeadsProfiler__Title__c_account',
        'LeadsProfiler__Title_ref__c_account',
        'LeadsProfiler__Vertical__c_account',
        'LeadsProfiler__Vertical_ref__c_account',
        'LeadsProfiler__OriginalRank__c_contact',
        'LeadsProfiler__Score__c_contact',
        'Best_Service_LevelOn__c',
        'Total_Gold_License__c',
        'Total_Mission_Critical__c',
        'Total_Platinum_License__c',
        'iKOCompanyName',
        'iKOCompanyPhone',
        'iKOCompanySize',
        'iKOCompanyWebsite',
        'iKOCountry',
        'iKOEmailMain',
        'iKOFirstName',
        'iKOInsertTime',
        'iKOJobCategory',
        'iKOJobTitle',
        'iKOLastName',
        'iKOLeadIndustry',
        'iKOLeadOwner',
        'iKOLeadPhone',
        'Interest_DP__c',
        'campaign_creative',
        'Opp_Created_After_Added_to_Conversica__c',
        'Is_Current_License_Expired__c',
        'successfactors_id__c',
        'successfactors_id__c_contact',
        'Website_behavior_summary__c',
        'HW__c',
        'MapR__c',
        'Teradata_EDW_Teradata_TDH_Teradata__c',
        'AWS_AWS_Redshift_AWS_EMR_AWS_spar__c',
        'Google_Google_BigQuery_Google_DataP__c',
        'HP_Vertica__c',
        'MongoDB__c',
        'DataStax__c',
        'Tableau__c',
        'Couchbase__c',
        'Qlik__c',
        'CDH__c',
        'NS_Transaction_Customer__c',
        'CSM_Team_Manager__c',
        'Customer_One_Drive_Location__c',
        'Do_not_allow_super_users__c',
        'Gainsight_C360__c',
        #'tic_username',
        'Date_of_1st_Renewal_Sale__c',
        'Lead_Source_2__c',
        'mktoLeadOwnerFirstName',
        'mktoLeadOwnerLastName',
        'mktoLeadOwnerEmailAddress',
        'mktoLeadOwnerPhoneNumber',
        'mktoLeadOwnerFullname',
        'SalesPredict_AWS__c',
        'Legacy_User__c',
        'SD_Company_Name__c',
        'Preferred_Language__c',
        'Top_Priority__c',
        'Top_Customer__c',
        'SDR__c',
        'behavior_Score_at_MQL',
        'predictive_Rank_at_MQL',
        'lead_Score_at_MQL',
        'SalesPredict_Score_at_MQL',
        'sSMatched',
        'sSNotMatched',
        'Contact_License_Mismatch__c',
        'SDR_Email__c',
        'Converted_to_Opportunity__c',
        'Contact_License_Mismatch_reseller__c',
        'Converted_to_ContactC__c',
        'X1_Inquiry_date__c',
        'X2_Ready_for_Review_Date__c',
        'X3_Working_Date__c',
        'X4_Qualifying_Date__c',
        'X5_Qualified_Date__c',
        'X6_Recycle_Date__c',
        'X7_Do_Not_Contact_Date__c',
        'Acquisition_Asset_Type__c',
        'Acquisition_Campaign__c',
        'MQL_Asset_Type__c',
        'MQL_Campaign__c',
        'End_User_Contact__c',
        'Decision_Maker_Contact__c',
        'Linked_Account__c',
        'LeanData__A2B_Account__c',
        'LeanData__A2B_Group__c',
        'LeanData__Has_Matched__c',
        'LeanData__Marketing_Sys_Created_Date__c',
        'LeanData__Matched_Account_Annual_Revenue__c',
        'LeanData__Matched_Account_Billing_Country__c',
        'LeanData__Matched_Account_Billing_Postal_Code__c',
        'LeanData__Matched_Account_Billing_State__c',
        'LeanData__Matched_Account_Custom_Field_1__c',
        'LeanData__Matched_Account_Employees__c',
        'LeanData__Matched_Account_Industry__c',
        'LeanData__Matched_Account_Name__c',
        'LeanData__Matched_Account_Type__c',
        'LeanData__Matched_Account_Website__c',
        'LeanData__Matched_Account__c',
        'LeanData__Matched_Buyer_Persona__c',
        'LeanData__Matched_Lead__c',
        'LeanData__Reporting_Matched_Account__c',
        'LeanData__Reporting_Timestamp__c',
        'LeanData__Router_Status__c',
        'LeanData__Routing_Action__c',
        'LeanData__Routing_Status__c',
        'LeanData__Salesforce_Id__c',
        'LeanData__Search_Index__c',
        'LeanData__Search__c',
        'LeanData__Segment__c',
        'LeanData__Status_Info__c',
        'LeanData__Tag__c',
        'LeanData__LD_EmailDomain__c',
        'LeanData__LD_EmailDomains__c',
        'LeanData__Reporting_Customer__c',
        'LeanData__Reporting_Has_Opportunity__c',
        'LeanData__Reporting_Last_Marketing_Touch_Date__c',
        'LeanData__Reporting_Last_Sales_Touch_Date__c',
        'LeanData__Reporting_Recent_Marketing_Touches__c',
        'LeanData__Reporting_Target_Account_Number__c',
        'LeanData__Reporting_Target_Account__c',
        'LeanData__Reporting_Total_Leads_and_Contacts__c',
        'LeanData__Reporting_Total_Marketing_Touches__c',
        'LeanData__SLA__c',
        'LeanData__Scenario_1_Owner__c',
        'LeanData__Scenario_2_Owner__c',
        'LeanData__Scenario_3_Owner__c',
        'LeanData__Scenario_4_Owner__c',
        'LeanData__Search__c_account',
        'LeanData__Tag__c_account',
        'Convert_to_Contact__c',
        'BigDataSandbox',
        'DSCORGPKG__CUSTOM_COUNTRY__c',
        'DSCORGPKG__CUSTOM_STATE__c',
        'DSCORGPKG__Custom_Annual_Rev__c',
        'DSCORGPKG__Custom_Company_HQ__c',
        'DSCORGPKG__Custom_Emp_No__c',
        'DSCORGPKG__Custom_Fiscal_Year__c',
        'DSCORGPKG__Custom_ITBudget__c',
        'DSCORGPKG__Custom_ITEmp_c__c',
        'DSCORGPKG__Custom_LinkedUrl__c',
        'DSCORGPKG__Custom_Title__c',
        'DSCORGPKG__Locked_By_User__c',
        'DSCORGPKG__Cust_Fiscal_Year__c',
        'DSCORGPKG__Cust_IT_Budget__c',
        'DSCORGPKG__Custom_3yr__c',
        'DSCORGPKG__Custom_Country_Full_RA__c',
        'DSCORGPKG__Custom_Country_RA__c',
        'DSCORGPKG__Custom_DUNS__c',
        'DSCORGPKG__Custom_Emp_No__c_account',
        'DSCORGPKG__Custom_ITEmp__c',
        'DSCORGPKG__Custom_NOA__c',
        'DSCORGPKG__Custom_Revenue__c',
        'DSCORGPKG__Custom_State_Full_RA__c',
        'DSCORGPKG__Custom_State_RA__c',
        'DSCORGPKG__Custom_des__c',
        'DSCORGPKG__Locked_By_User__c_account',
        'DSCORGPKG__Custom_Address__c',
        'DSCORGPKG__Custom_Company_HQ_Address__c',
        'DSCORGPKG__Custom_Company_HQ_City__c',
        'DSCORGPKG__Custom_Country__c_contact',
        'DSCORGPKG__Custom_Phone__c',
        'DSCORGPKG__Custom_State__c_contact',
        'DSCORGPKG__REMOVELinkedinURL__c',
        'DSCORGPKG__title_Custom__c',
        'Talend_6_x__c',
        'Puchase_Influence_Level__c',
        'Author__c',
        'Survey_Language_Code__c',
        'CSM_User__c',
        'Current_Product_Version__c',
        'Follow_up_Escalation_Owner_1__c',
        'Market__c',
        'Product_Name__c',
        'Professional_Services__c',
        'Software_Upgrade__c',
        'Future_Theater__c',
        'Survey_Language_Code__c_contact',
        'Renewal_Check__c',
        'NPS_Check__c',
        'Purchase_Influence_Level__c',
        'Check__c',
        'Response_Rate_Notification_Recipient__c',
        'PrimaryScore__c',
        'AVA__AVAAI_action_required__c',
        'AVA__AVAAI_action_required_date__c',
        'AVA__AVAAI_conversation_stage__c',
        'AVA__AVAAI_conversation_stage_date__c',
        'AVA__AVAAI_conversation_status__c',
        'AVA__AVAAI_conversation_status_date__c',
        'AVA__AVAAI_conversica_lead_status__c',
        'AVA__AVAAI_conversica_lead_status_date__c',
        'cas__FirstAttempt__c',
        'cas__First_Conversation_Date__c',
        'cas__LastAttempt__c',
        'cas__Last_Connect__c',
        'cas__List_Name__c',
        'cas__Most_Recent_Attempt_Disposition__c',
        'cas__Most_Recent_Conversation_Disposition__c',
        'cas__Most_Recent_Disposition__c',
        'cas__NumberAttempts__c',
        'cas__NumberConnects__c',
        'cas__Penalty_Box_Status__c',
        'cas__ContactStatus__c',
        'Author_for_Opportunity__c',
        'NS_Account_Number__c',
        'Partner_portal_sourced__c',
        'Partner_portal_sourced__c_account',
        'Ctvt_CloseDate__c',
        'PartnerPortalSourced__c',
        'Lattice_Score__c',
        'Lattice_Timestamp__c',
        'Lattice_Webhook_Timestamp__c',
        'Ctvt_PartnerOrgName__c',
        'Ctvt_PartnerUserEmail__c',
        'Ctvt_CurrencyOfTheOpportunity_1_1__c',
        'Ctvt_Amount__c',
        'Ctvt_RegistrationStatus_1__c',
        'Ctvt_PartnerUserName__c',
        'Ctvt_Stage__c',
        'Ctvt_Title__c',
        'Ctvt_ProjectBudgetInLocalCurrency_1__c',
        'Ctvt_PartnerUserPhone__c',
        'Ctvt_TimelineOtherDatesAndDeadlines_1__c',
        'Ctvt_SummaryOfTheTechnicalEnvironme_1__c',
        'Ctvt_Sys_EntityType__c',
        'Ctvt_Sys_URL__c',
        'Ctvt_HowCanTalendHelpYouWithYourCus_1__c',
        'Ctvt_Sys_LastUpdated__c',
        'Ctvt_CurrentEngagementWithTheCustom_1__c',
        'Ctvt_EngagementHistoryWithTheCustom_1__c',
        'Ctvt_AnyOtherInformation_1__c',
        'Ctvt_SummaryOfTheDealopportunityKey_1__c',
        'Ctvt_DidYouTalkToATalendRepIfSoPlea_1__c',
        'LBI__EstimatedRevenue__c',
        'LBI__LatticeRating__c',
        'LBI__Recommendation__c',
        'LBI__AccountExtension__c',
        'LBI__NumberOfOpenInProgressRecommendations__c',
        'LBI__AccountName__c',
        'Lattice_Rank__c',
        'jobFunction2',
        'Critical_Account__c',
        'NPS_Check_Accts_up_for_Renewal__c',
        'Quarter__c',
        'Today_s_Quarter__c',
        'cventJobTitle',
        'cventAdmissionItem',
        'cventRegistrationType',
        'cventRegistrationStatus',
        'cventConfirmation',
        'cventRegistrationDate',
        'Ctvt_Description_1__c',
        'Ctvt_AnyOtherInformation_2__c',
        'Sales_Activities_Since_Last_MQL__c',
        'Latitude',
        'Longitude',
        'GeocodeAccuracy',
        'Address',
        'PhotoUrl',
        'LastViewedDate',
        'LastReferencedDate',
        'JigsawContactId_lead',
        'CleanStatus',
        'CompanyDunsNumber',
        'BillingLatitude',
        'BillingLongitude',
        'BillingGeocodeAccuracy',
        'BillingAddress',
        'ShippingLatitude',
        'ShippingLongitude',
        'ShippingGeocodeAccuracy',
        'ShippingAddress',
        'PhotoUrl_account',
        'LastViewedDate_account',
        'LastReferencedDate_account',
        'JigsawCompanyId_account',
        'CleanStatus_account',
        'AccountSource',
        'DunsNumber',
        'Tradestyle',
        'NaicsCode',
        'NaicsDesc',
        'YearStarted',
        'SicDesc',
        'OtherLatitude',
        'OtherLongitude',
        'OtherGeocodeAccuracy',
        'OtherAddress',
        'MailingLatitude',
        'MailingLongitude',
        'MailingGeocodeAccuracy',
        'MailingAddress',
        'IsEmailBounced',
        'Ctvt_AdditionalInformation_1__c',
        'Ctvt_HowCanTalendAssistYouWithYourC__c',
        'LIM_since_Recycle__c',
        'leadCodeCustom',
        'First_Activity__c',
        'Lattice_Behavioral_Score__c',
        'Lattice_Behavioral_Timestamp__c',
        'Lattice_Behavioral_Rating__c',
        'Assigned_CSMs__c',
        'Lattice_Fit_Behavior__c',
        'Lattice_Fit_Behavior_Timestamp__c',
        'Awareness_Campaign_Sent__c',
        'DP_included_in_on_boarding__c',
        'Info_Requested__c',
        'Demo_Requested__c',
        'POC_Requested__c',
        'Free_Licenses_activated__c',
        'DP_in_Prod_Use__c',
        'rrpu__Alert_Message__c',
        'rrpu__Alert_Message__c_account',
        'LPI_Cloud_Infrastructure_Tech__c',
        'LPI_Cloud_Service_Tier_1__c',
        'LPI_Cloud_Service_Tier_2__c',
        'LBI_Cloud_Infrastructure_Tech__c',
        'LBI_Cloud_Service_Tier_1__c',
        'LBI_Cloud_Service_Tier_2__c',
        'LPI_Has_Adobe_Target_Standard__c',
        'LPI_Has_Amazon_AWS__c',
        'LBI_Has_Amazon_Redshift__c',
        'LPI_Has_Apache_Hadoop__c',
        'LBI_Has_Apache_Hive__c',
        'LBI_Has_Cloudera__c',
        'LBI_Has_CoolaData__c',
        'LBI_Has_IBM_InfoSphere_DataStage__c',
        'LBI_Has_Informatica__c',
        'LBI_Has_Loggly__c',
        'LBI_Has_Mulesoft__c',
        'LBI_Has_Rekko__c',
        'LBI_Has_TellApart__c',
        'LBI_Has_Adobe_Target_Standard__c',
        'LBI_Has_Amazon_AWS__c',
        'LBI_Has_Apache_Hadoop__c',
        'Express_Consent__c',
        'Express_Consent_History__c',
        'Inferred_Consent__c',
        'Inferred_Consent_History__c',
        'Created_By_Role__c',
        'Global_Account__c',
        'Regional_AE__c',
        'First_MQL_Date__c',
        'Not_Interested__c',
        'Date_of_Last_Data_Prep_Conversation__c',
        'Active_User_Status__c',
        'temp_assignment',
        'Ctvt_RenewalOpportunity__c',
        'Ctvt_BrandNewOpportunity__c',
        'Chat_Transcript__c',
        'Chat_Agent_ID__c',
        'Payment_Term__c',
        'Customer_Acquisition_Date__c',
        'Account_ID_long__c',
        'LMS_Student_ID__c',
        'Actual_Users__c',
        'Are_you_using_Joblets__c',
        'Big_Data_Components__c',
        'Big_Data_Streaming_in_Use__c',
        'Building_Actions__c',
        'Building_Map_Reduce_of_Spark_Batch_Jobs__c',
        'Building_Mediation_Routes__c',
        'Building_SOAP_or_REST_Services__c',
        'Building_a_Lambda_Kappa_Zeta_Arch__c',
        'Cloud_Environment__c',
        'Completed_Training__c',
        'DEV__c',
        'Data_Cleansing_Masking_Used__c',
        'Database_Type__c',
        'Develop_Using_Spring_DLS__c',
        'Disaster_Recovery__c',
        'EOL_12_months__c',
        'Engaged__c',
        'Finite_Project__c',
        'Hadoop_Components_Used__c',
        'How_many_data_stewards__c',
        'Implementation_Approach__c',
        'Implementation__c',
        'In_Production__c',
        'Java_Version__c',
        'MDMs_Driving_Critical_Business_Processes__c',
        'Open_Feature_Request__c',
        'Operating_System__c',
        'Pre_Production__c',
        'Product_Deployed_in_the_Cloud__c',
        'Production__c',
        'Referenceable__c',
        'System_Integration_Test__c',
        'TAC_Users__c',
        'TEST__c',
        'User_Acceptance_Test__c',
        'Using_All_Licenses__c',
        'Using_All_Products__c',
        'Using_Big_Data_Components__c',
        'Using_ML_Algorithms_or_Components__c',
        'Using_Metadata_Bridge__c',
        'Using_Profiling_features_of_the_Studio__c',
        'Using_Spark_Streaming__c',
        'Using_TAC_in_Development__c',
        'Using_TAC_in_High_Availability__c',
        'Using_TAC_in_Production__c',
        'Using_Talend_Data_Mapper__c',
        'Using_Talend_Data_Prep_2_Free_Licenses__c',
        'Using_Virtual_Servers_Groups__c',
        'Version__c',
        'of_Dev_Ops_Admin_Ops_Users__c',
        'of_Environments__c',
        'of_Studio_Users__c',
        'of_Testers__c',
        'Usage_Rate__c',
        'Customer_Success_SharePoint_Search__c',
        'personTimeZone',
        'Account_Discount__c',
        'Account_Services_Discount__c',
        'AVA_SFCPQ__ExemptEntityType__c',
        'AVA_SFCPQ__TaxExemptionCode__c',
        'Account_Has_Cust_Terms__c',
        'tICDataCenterLocation',
        'tICAcceptTerms',
        'dataLakeAccelerator',
        'Remove_Account__c',
        'Acct_Revenue_MAX__c',
        'Total_Opps_Stage_2__c',
        'Partner_Status__c',
        'Premier_Partner__c',
        'Partner_Level__c',
        'Lead__c',
        'Account__c',
        'Dietary_Requirements',
        'qbdialer__Related_Contact_Dials__c',
        'qbdialer__Related_Contact_LastCallTime__c',
        'Primary_Partner_Level__c',
        'Primary_Partner_Owner__c',
        'Primary_Partner_Type__c',
        'Primary_Premier_Partner__c',
        'Sourcing_Partner__c',
        'MQL_Date_Time_Last__c',
        'bTLKLevel',
        'bTLKUserID',
        'bTLKLeadContext',
        'bTLKLeadType',
        'bTLKReferral',
        'bTLKChannelID',
        'bTLKChannelName',
        'bTLKChannelOrganization',
        'bTLKChannelsBrightTALKURL',
        'bTLKEngagementScore',
        'bTLKTimeZone',
        'bTLKEmbedMarketoToken',
        'bTLKEmbedURL',
        'bTLKEmbedUTMSource',
        'bTLKEmbedUTMTerm',
        'bTLKEmbedUTMMedium',
        'bTLKEmbedUTMContent',
        'bTLKEmbedUTMCampaign',
        'bTLKActivityType',
        'bTLKWebcastID',
        'bTLKWebcastURL',
        'bTLKWebcastTitle',
        'bTLKLastActivityDate',
        'bTLKLiveMinutesViewed',
        'bTLKRecordedMinutesViewed',
        'bTLKTotalMinutesViewed',
        'bTLKViewingURL',
        'bTLKUTMSource',
        'bTLKUTMTerm',
        'bTLKUTMMedium',
        'bTLKUTMContent',
        'bTLKUTMCampaign',
        'bTLKWebcastPresenter',
        'bTLKWebcastDuration',
        'bTLKWebcastDurationMinutes',
        'bTLKCreatedDate',
        'bTLKPreregistered',
        'bTLKLiveViewingDuration',
        'bTLKLiveViewingsCount',
        'bTLKRecordedViewingDuration',
        'bTLKRecordedViewingsCount',
        'bTLKTotalViewingDuration',
        'bTLKTotalViewingsCount',
        'bTLKMarketoToken',
        'bTLKAttachmentID',
        'bTLKAttachmentTitle',
        'bTLKAttachmentType',
        'bTLKAttachmentURL',
        'bTLKFirstAccessedDate',
        'bTLKAttachmentActivityID',
        'bTLKLastAccessedDate',
        'bTLKLiveViewAccessCount',
        'bTLKRecordedAccessCount',
        'bTLKTotalAccessCount',
        'bTLKLastAccessURL',
        'bTLKLastAccessMarketoToken',
        'bTLKLastAccessUTMCampaign',
        'bTLKLastAccessUTMContent',
        'bTLKLastAccessUTMMedium',
        'bTLKLastAccessUTMSource',
        'bTLKLastAccessUTMTerm',
        'First_Activity_Time__c',
        'Total_Activities_Including_Outreach_Dia__c',
        'Total_Activities_MQL_With_Outreach__c',
        'Total_Number_of_Activities__c',
        'Total_Number_of_Activities_since_MQL__c',
        'ddc_prospector__Sourced_from_Data_com__c',
        'ddc_prospector__Sourced_from_Data_com__c_account',
        'ddc_prospector__Sourced_from_Data_com__c_contact',
        'Contacts_Previous_Experience__c',
        'Secondary_Account_Revenue__c',
        'Secondary_Account_Revenue_Source__c',
        'Contact_ID_long__c',
        'Resource_URL',
        'Resource_Name',
        'Resource_ID',
        'Account_Segment_CFY__c',
        'Is_Domestic_Parent__c',
        'Domestic_Parent__c']):

        records1 = pandas.DataFrame(index=range(0, len(leads)),
                                    columns=[
                                        'id',
                                        'firstName',
                                        'middleName',
                                        'lastName',
                                        'email',
                                        'company',
                                        'site',
                                        'street',
                                        'city',
                                        'state',
                                        'country',
                                        'postalCode',
                                        'website',
                                        'mainPhone',
                                        'annualRevenue',
                                        'numberOfEmployees',
                                        'industry',
                                        'sicCode',
                                        'mktoCompanyNotes',
                                        'sfdcAccountId',
                                        'mktoName',
                                        'personType',
                                        'mktoIsPartner',
                                        'isLead',
                                        'mktoIsCustomer',
                                        'isAnonymous',
                                        'salutation',
                                        'phone',
                                        'mobilePhone',
                                        'fax',
                                        'title',
                                        'contactCompany',
                                        'dateOfBirth',
                                        'personPrimaryLeadInterest',
                                        'originalSourceType',
                                        'originalSourceInfo',
                                        'registrationSourceType',
                                        'registrationSourceInfo',
                                        'originalSearchEngine',
                                        'originalSearchPhrase',
                                        'originalReferrer',
                                        'emailInvalid',
                                        'emailInvalidCause',
                                        'unsubscribed',
                                        'unsubscribedReason',
                                        'doNotCall',
                                        'mktoDoNotCallCause',
                                        'doNotCallReason',
                                        'mktoPersonNotes',
                                        'sfdcType',
                                        'sfdcContactId',
                                        'anonymousIP',
                                        'inferredCompany',
                                        'inferredCountry',
                                        'inferredCity',
                                        'inferredStateRegion',
                                        'inferredPostalCode',
                                        'inferredMetropolitanArea',
                                        'inferredPhoneAreaCode',
                                        'createdAt',
                                        'updatedAt',
                                        'leadPerson',
                                        'leadRole',
                                        'leadSource',
                                        'leadStatus',
                                        'leadScore',
                                        'urgency',
                                        'priority',
                                        'relativeScore',
                                        'relativeUrgency',
                                        'rating',
                                        'sfdcLeadId',
                                        'sfdcLeadOwnerId',
                                        'leadPartitionId',
                                        'leadRevenueCycleModelId',
                                        'leadRevenueStageId',
                                        'Interest_DI',
                                        'Interest_DQ',
                                        'Interest_MDM',
                                        'Interest_ESB',
                                        'Sugar_lead_id',
                                        'Sugar_cid',
                                        'Business_zone',
                                        'Phone_office_valid',
                                        'Phone_mobile_valid',
                                        'Language_preference',
                                        'Phone_extension',
                                        'Department',
                                        'Status_in_CRM',
                                        'BDR_interest_determination',
                                        'Bounced_elsewhere',
                                        'Account_potential',
                                        'acquisitionProgramId',
                                        'mktoAcquisitionDate',
                                        'Test',
                                        'LastScoring-Adoption',
                                        'jigsawContactStatus',
                                        'jigsawContactId',
                                        'sfdcId',
                                        'Interest_TIF',
                                        'Interest_TFS',
                                        'LastInteractionDate',
                                        'JobFunction',
                                        'PrimaryProductInterest',
                                        'LeadComments',
                                        'SalesAlert',
                                        'Alert',
                                        'Third-PartySource',
                                        'Marketo_SFDC_Id',
                                        'NetSuiteId',
                                        'SendtoNetsuite',
                                        'Push_to_Sales',
                                        'NS_Email',
                                        'AccountType',
                                        'Territory',
                                        'Job_Level',
                                        'Use_Case',
                                        'Last_Scoring_UserDoc',
                                        'Last_Scoring_ProductReg',
                                        'Last_Scoring_Tutorial',
                                        'Adoption_Level',
                                        'jigsawCompanyStatus',
                                        'jigsawCompanyId',
                                        'Nurture_Campaign_Assigned',
                                        'Alert_Date',
                                        'Lead_Comment_History',
                                        'Indicated_Industry',
                                        'SD_Company_Name',
                                        'SD_Company_Address',
                                        'SD_Company_State',
                                        'SD_Company_Postal_Code',
                                        'SD_Company_Country',
                                        'SD_Company_Phone',
                                        'SD_Source',
                                        'SD_ID',
                                        'SD_Date',
                                        'SD_Match_Confidence',
                                        'SD_Company_Fax',
                                        'SD_Entity_Type',
                                        'SD_Business_Description',
                                        'SD_Ultimate_Parent_ID',
                                        'SD_Ultimate_Parent_Name',
                                        'NAIC_Code',
                                        'SD_Revenue_Currency',
                                        'SD_Assets_USD',
                                        'SD_Company_Stock_Exchange',
                                        'SD_Company_Ticker_Symbol',
                                        'SD_Number_Employees',
                                        'ProductVersion',
                                        'Telemarketing_Status',
                                        'Interest_BPM',
                                        'Interest_BigData',
                                        'Phone_Invalid',
                                        'PostalCode_Invalid',
                                        'EmailInvalid_API',
                                        'CurrentNurtureProgram',
                                        'Asset',
                                        'Username',
                                        'LeadSelf-Identifier',
                                        'RoadshowChoice1',
                                        'RoadshowChoice2',
                                        'Asset_History',
                                        'gender',
                                        'facebookDisplayName',
                                        'twitterDisplayName',
                                        'linkedInDisplayName',
                                        'facebookProfileURL',
                                        'twitterProfileURL',
                                        'linkedInProfileURL',
                                        'facebookPhotoURL',
                                        'twitterPhotoURL',
                                        'linkedInPhotoURL',
                                        'facebookReach',
                                        'twitterReach',
                                        'linkedInReach',
                                        'facebookReferredVisits',
                                        'twitterReferredVisits',
                                        'linkedInReferredVisits',
                                        'totalReferredVisits',
                                        'facebookReferredEnrollments',
                                        'twitterReferredEnrollments',
                                        'linkedInReferredEnrollments',
                                        'totalReferredEnrollments',
                                        'lastReferredVisit',
                                        'lastReferredEnrollment',
                                        #'TalendEmployee',
                                        'TimeSlot',
                                        'TimeSlot2',
                                        'syndicationId',
                                        'CampaignSource',
                                        'CampaignMedium',
                                        'CampaignTerm',
                                        'CampaignID',
                                        'Registered_BD',
                                        'Registered_ESB',
                                        'Registered_MDM',
                                        'Registered_DQ',
                                        'Registered_DI',
                                        'CampaignContent',
                                        'RegisteredProductName',
                                        'ProductNameRecognized',
                                        'RegisteredProducts',
                                        'RegisteredProductType',
                                        'ForumNotes',
                                        'RoadshowChoice3',
                                        'QualifiedUser',
                                        'LeadSourceDetail',
                                        'upgradeinterest',
                                        'facebookId',
                                        'twitterId',
                                        'linkedInId',
                                        'Rep_First_Name',
                                        'Rep_Last_Name',
                                        'Rep_Email_Address',
                                        'Rep_Job_Title',
                                        'Behavior_Score',
                                        'Demographic_Score',
                                        'Product_Evaluation_Request',
                                        'Product_Evaluation_Request_History',
                                        'Last_Product_Evaluation_Request_Date',
                                        'Product_Evaluation_Request_Activity_Log',
                                        'TechTarget_AI_Contact_Link',
                                        'Nurture_Program_Changed',
                                        'Named_Account',
                                        'Rep_Phone_Number',
                                        'nurture_campaign_flow_stop',
                                        'nurture_campaign_flow_start',
                                        'sandboxInstance',
                                        'cookies',
                                        'CurrencyIsoCode',
                                        'EmailBouncedReason',
                                        'EmailBouncedDate',
                                        'DSCORGPKG__DeletedFromDiscoverOrg__c',
                                        'DSCORGPKG__DiscoverOrg_Company_ID__c',
                                        'DSCORGPKG__DiscoverOrg_ID__c',
                                        'DSCORGPKG__DiscoverOrg_Technologies__c',
                                        'DSCORGPKG__ITOrgChart__c',
                                        'DSCORGPKG__LinkedIn_URL__c',
                                        'DSCORGPKG__ReportsTo__c',
                                        'DSCORGPKG__Twitter_URL__c',
                                        'Alert_Phone__c',
                                        'Competition__c',
                                        'Do_Not_Call_Reason__c',
                                        'Function_called_Job_Function_in_Marketo__c',
                                        'Job_Role__c',
                                        'LinkedIn_URL__c',
                                        'MQL_Channel__c',
                                        'MQL_Date__c',
                                        'MQL_Program__c',
                                        'Mobile_Phone__c',
                                        'Notes_for_Marketing_Only__c',
                                        'Nurture_Return__c',
                                        'Other_Competition__c',
                                        'Phone_Business__c',
                                        'Phone_Extension_Business__c',
                                        'Reason_Code__c',
                                        'RegionF__c',
                                        'Region__c',
                                        'mkto_si__HideDate__c',
                                        'mkto_si__MSIContactId__c',
                                        'CurrencyIsoCode_account',
                                        'Channel_tier__c_account',
                                        'Customer_Type__c',
                                        'Region__c_account',
                                        'DSCORGPKG__DiscoverOrg_ID__c_account',
                                        'Account_Potential__c_account',
                                        'Account_Subsidiary__c',
                                        'Competition__c_account',
                                        'Language__c',
                                        'Other_Competition__c_account',
                                        'CurrencyIsoCode_contact',
                                        'Alt_Email__c',
                                        'Function__c',
                                        'Use_Case__c_contact',
                                        'mkto_si__Sales_Insight__c',
                                        'lastProgramChannel',
                                        'lastProgram',
                                        'acquisitionChannel',
                                        'Eval_EULA',
                                        'recycled_date',
                                        'pushtoNetSuite',
                                        'Country__c',
                                        'Lead_Lifecyle__c',
                                        'MQL_Program_X__c',
                                        'Sales_Activities_MQL__c',
                                        'Sourced_Industry__c',
                                        'Sourced_Phone__c',
                                        'State__c',
                                        'Subsidiary_Auto__c',
                                        'Territory__c',
                                        'RecordTypeId',
                                        'Oppstageflag__c',
                                        'Contact_Status__c',
                                        'Converted_Department__c',
                                        'MQL_Offer_Name',
                                        #'Channel_Offer',
                                        'Marketo_Lead_ID',
                                        'mktomerge',
                                        'External_Id__c',
                                        'Subsidiary__c_contact',
                                        'Salesforce_Internal_Id__c',
                                        'Date_of_First_Sale__c',
                                        'Push_To_NetSuite_Reason__c',
                                        'Contact_Us_Reason__c',
                                        'VAT_ID__c',
                                        'NS_Account_Owner__c',
                                        'Parent_Acct__c',
                                        'SF_Customer_Number__c',
                                        'Customer_Health__c',
                                        'Customer_Tier__c',
                                        'Territory_Focus__c',
                                        'Country_Group__c',
                                        'Account_Currency_Formula__c',
                                        'User_Subsidiary__c',
                                        'CSM_Customer_Description__c',
                                        'Health_Reason__c',
                                        'Salesforce_Internal_Id_del__c',
                                        'RecordTypeId_lead',
                                        'Job_Function__c',
                                        'Domain_group__c',
                                        'Country__c_account',
                                        'Owner_NetSuite_Id__c',
                                        'Outdated_Region__c',
                                        'Hours_Since_MQL__c',
                                        'companySFDC',
                                        'lastNameSFDC',
                                        'Opportunity__c',
                                        'cSMFullName',
                                        'Lead_Qualification_Date__c',
                                        'download_status',
                                        'Company_HQ_Location_State_Province__c',
                                        'Channel__c',
                                        'Channel_Partner__c',
                                        'Account_Description__c',
                                        'Account_Tier__c',
                                        'Health_Score__c',
                                        'Health_Required_Actions__c',
                                        'Health_Action_Ownership__c',
                                        'Health_Action_Status__c',
                                        'Renewal_Risk__c',
                                        'Renewal_Risk_Comment__c',
                                        'Upsell_Risk__c',
                                        'Upsell_Risk_Comment__c',
                                        'Customer_Sat_Risk__c',
                                        'Customer_Sat_Risk_Comment__c',
                                        'Competitive_Threat_Risk__c',
                                        'Competitive_Threat_Risk_Comment__c',
                                        'Strategic_Relationship_Risk__c',
                                        'Strategic_Relationship_Risk_Comment__c',
                                        'Adoption_Risk__c',
                                        'Adoption_Risk_Comment__c',
                                        'Proven_Value_Risk__c',
                                        'Proven_Value_Risk_Comment__c',
                                        'Other_Risk__c',
                                        'Other_Risk_Comment__c',
                                        'Deployment_Progress__c',
                                        'Laster_QBR__c',
                                        'Next_QBR__c',
                                        'Assigned_CSM__c',
                                        'LID__LinkedIn_Company_Id__c',
                                        'LID__LinkedIn_Member_Token__c',
                                        'LID__LinkedIn_Company_Id__c_account',
                                        'qbdialer__Dials__c',
                                        'qbdialer__LastCallTime__c',
                                        'qbdialer__ResponseTime__c',
                                        'qbdialer__Dials__c_account',
                                        'qbdialer__LastCallTime__c_account',
                                        'qbdialer__ResponseTime__c_account',
                                        'UniqueEntry__Contact_Dupes_Ignored__c',
                                        'UniqueEntry__Lead_Dupes_Ignored__c',
                                        'UniqueEntry__Account_Dupes_Ignored__c',
                                        'preMQLProgramAttribution',
                                        'mQLProgramAttribution',
                                        'sQLProgramAttribution',
                                        'sALProgramAttribution',
                                        'winProgramAttribution',
                                        'Days_Since_MQLs__c',
                                        'Days_Since_MQLs_del__c',
                                        'interestTIC',
                                        'TIC_Credentials_Issue_Date__c',
                                        'NanoCloud_Account_Created_Date__c',
                                        'of_calls_per_lead__c',
                                        'companySFDCClone',
                                        'lastNameSFDCClone',
                                        'acquisition_Channel_temp',
                                        'updatedFromAPI',
                                        'RingLead_Status',
                                        'mKTOdummyfield',
                                        'MQL_Program_temp',
                                        'revenueCycleDatesKnown',
                                        'revenueCycleDatesEngaged',
                                        'revenueCycleDatesMQL',
                                        'revenueCycleDatesASDRAccepted',
                                        'revenueCycleDatesSQL',
                                        'revenueCycleDatesPipeline',
                                        'revenueCycleDatesBestCase',
                                        'revenueCycleDatesCommit',
                                        'revenueCycleDatesCustomer',
                                        'revenueCycleDatesRenewal',
                                        'revenueCycleDatesUpsell',
                                        'revenueCycleDatesExpired',
                                        'revenueCycleDatesInactive',
                                        'revenueCycleDatesBadData',
                                        'revenueCycleDatesUnqualified',
                                        'revenueCycleDatesRecycled',
                                        'revenueCycleDatesReturntoADR',
                                        'revenueCycleDatesLost',
                                        'revenueCycleCurrentStage',
                                        'SD_Lead_Notes__c',
                                        'SD_Company_Address__c',
                                        'SD_Company_City__c',
                                        'SD_Business_Description__c',
                                        'SD_Company_Country__c',
                                        'SD_IT_Budget__c',
                                        'SD_IT_Employees__c',
                                        'SD_Company_Postal_Code__c',
                                        'SD_Tech_Business_Intelligence__c',
                                        'SD_Tech_CRM_MarketingAutomation__c',
                                        'SD_Tech_DataManagement__c',
                                        'SD_Tech_Data_Storage__c',
                                        'SD_Tech_Databases__c',
                                        'SD_Tech_ERP_HR_HCM_FI__c',
                                        'SD_Tech_Enterprise_Applications__c',
                                        'SD_Tech_Hardware_OS_SystemsEnvironment__c',
                                        'SD_Tech_ITSM__c',
                                        'SD_Tech_Languages__c',
                                        'SD_Tech_Programming_Tools__c',
                                        'SD_Company_Address__c_contact',
                                        'SD_Company_City__c_contact',
                                        'SD_Company_Postal_Code__c_contact',
                                        'Phone_1st_3_Digits__c',
                                        'Sales_Activities_MQL_Dials__c',
                                        'i__CreatedForUser__c',
                                        'i__DaysSinceLastMail__c',
                                        'i__LastInboundMail__c',
                                        'i__LastInboundSent__c',
                                        'i__LastInboundTime__c',
                                        'i__LastMailSent__c',
                                        'i__LastMailTimeDelta__c',
                                        'i__LastMailTime__c',
                                        'i__LastMail__c',
                                        'i__LastOutboundMail__c',
                                        'i__LastOutboundSent__c',
                                        'i__LastOutboundTime__c',
                                        'i__OtherEmails__c',
                                        'i__DaysSinceLastMail__c_account',
                                        'i__LastInboundMail__c_account',
                                        'i__LastInboundSent__c_account',
                                        'i__LastInboundTime__c_account',
                                        'i__LastMailSent__c_account',
                                        'i__LastMailTimeDelta__c_account',
                                        'i__LastMailTime__c_account',
                                        'i__LastMail__c_account',
                                        'i__LastOutboundMail__c_account',
                                        'i__LastOutboundSent__c_account',
                                        'i__LastOutboundTime__c_account',
                                        'mktotempfield',
                                        'sDITBudgetC',
                                        'sDITEmployeesC',
                                        'sDTechBusinessIntelligenceC',
                                        'sDTechCRMMarketingAutomationC',
                                        'sDTechDataManagementC',
                                        'sDTechDataStorageC',
                                        'sDTechDatabasesC',
                                        'sDTechERPHRHCMFIC',
                                        'sDTechEnterpriseApplicationsC',
                                        'sDTechHardwareOSSystemsEnvironmentC',
                                        'sDTechITSMC',
                                        'sDTechLanguagesC',
                                        'sDTechProgrammingToolsC',
                                        'sDBusinessDescriptionC',
                                        'sDCompanyCountryC',
                                        'mostRecentLeadSource',
                                        'mostRecentLeadSourceDetail',
                                        'Product_Solution_Integration_Cloud__c',
                                        'updateFromDiscoverOrg',
                                        'qbdialer__CloseDate__c',
                                        'qbdialer__CloseScore__c',
                                        'qbdialer__ContactDate__c',
                                        'qbdialer__ContactScoreId__c',
                                        'qbdialer__ContactScore__c',
                                        'qbdialer__TimeZoneSidKey__c',
                                        'qbdialer__TimeZoneSidKey__c_account',
                                        'NPS_Contact__c',
                                        'Executive_Sponsor__c',
                                        'Gainsight_Health__c',
                                        'Renewal_Status__c',
                                        'Renewal_Type__c',
                                        'externalCompanyId',
                                        'sf_leadid__c',
                                        'sf_contactid__c',
                                        'Mass_Update_for_Marketo__c',
                                        'DSCORGPKG__DiscoverOrg_Created_On__c',
                                        'DSCORGPKG__External_DiscoverOrg_Id__c',
                                        'DSCORGPKG__department__c',
                                        'DSCORGPKG__DiscoverOrg_Created_On__c_account',
                                        'DSCORGPKG__External_DiscoverOrg_Id__c_account',
                                        'Renew_Loss__c',
                                        'Customer_Categorization__c',
                                        'reasonsNotPromoted',
                                        'CAB_Member__c',
                                        'White_Glove__c',
                                        'X1_How_is_the_customer_measuring_success__c',
                                        'X2_Are_they_we_achieving_that_success__c',
                                        'X3_How_has_their_experience_been__c',
                                        'externalSalesPersonId',
                                        'End_User_ACV__c',
                                        'End_User_TCV__c',
                                        'Partner_ACV__c',
                                        'Partner_TCV__c',
                                        'Reseller_ACV__c',
                                        'Reseller_TCV__c',
                                        'aWSUsage',
                                        'aWSInfoShare',
                                        'qbdialer__CloseDate__c_account',
                                        'qbdialer__CloseScore__c_account',
                                        'CSM_Email_Address__c',
                                        'CSM_Phone_Number__c',
                                        'Account_Channel_Tier__c',
                                        'landing_page_language',
                                        'Assigned_CSA__c',
                                        'Buyer_Journey_Stage__c',
                                        'AVA__AVAAI_date_added__c',
                                        'AVA__AVAAI_first_message_date__c',
                                        'AVA__AVAAI_hot_lead__c',
                                        'AVA__AVAAI_hot_lead_date__c',
                                        'AVA__AVAAI_last_message_date__c',
                                        'AVA__AVAAI_last_response_date__c',
                                        'AVA__AVAAI_lead_at_risk__c',
                                        'AVA__AVAAI_lead_at_risk_date__c',
                                        'AVA__AVAAI_options__c',
                                        'AVA__AVAAI_score__c',
                                        'AVA__AVAAI_status__c',
                                        'AVA__Campaign__c',
                                        'IsPartner',
                                        'IsCustomerPortal',
                                        'Account_OTRS_ID__c',
                                        'Total_Active_User_Support_Licenses__c',
                                        'Total_Portal_Support_Users__c',
                                        'Customer_Preferred_Region__c',
                                        'Active_Support_User__c',
                                        'License_Company_Name__c',
                                        'License_End_Date__c',
                                        'License_Start_Date__c',
                                        'Primary_Support_Contact__c',
                                        'Tier__c',
                                        'Support_Contact__c',
                                        'customer_id__c',
                                        'License_Service_Level__c',
                                        'account_code',
                                        'Executive_Contact__c',
                                        'Champion_Contact__c',
                                        'Billing_Contact__c',
                                        'Reference_Contact__c',
                                        'Architect_Contact__c',
                                        'Total_Opportunities__c',
                                        'Total_Open_Opportunities__c',
                                        'Super_Contact_User__c',
                                        'Conversica_Outreach_Context__c',
                                        'Conversica_Inquiry_Verb__c',
                                        'Conversica_Outreach_Title__c',
                                        'CSM_Brief_Company_Overview__c',
                                        'CSM_Brief_Background_on_Account__c',
                                        'CSM_Business_Case_Why_Talend__c',
                                        'CSM_Competitive_Landscape__c',
                                        'A_Initial_Adoption_Usage__c',
                                        'A_Initial_Business_Case__c',
                                        'A_Initial_Success_Criteria__c',
                                        'A_Initial_Use_Case__c',
                                        'D_Initial_Adoption_Usage__c',
                                        'D_Initial_Business_Case__c',
                                        'D_Initial_Success_Criteria__c',
                                        'D_Initial_Use_Case__c',
                                        'E_Initial_Deployment__c',
                                        'M_Initial_Business_Case_Location__c',
                                        'M_Initial_Success_Criteria_Location__c',
                                        'M_Initial_Use_Case_Location__c',
                                        'MAE_Presentation_URL__c',
                                        'MAE_Record_Session_URL__c',
                                        'Web_User_Login__c',
                                        'LeadsProfiler__Business_Group__c',
                                        'LeadsProfiler__Business_Group_ref__c',
                                        'LeadsProfiler__Buyer_Persona__c',
                                        'LeadsProfiler__Buyer_Persona_ref__c',
                                        'LeadsProfiler__ChangeRankReason__c',
                                        'LeadsProfiler__City__c',
                                        'LeadsProfiler__City_ref__c',
                                        'LeadsProfiler__Company_Profile__c',
                                        'LeadsProfiler__Company_Profile_ref__c',
                                        'LeadsProfiler__Company_Revenue__c',
                                        'LeadsProfiler__Company_Revenue_ref__c',
                                        'LeadsProfiler__Company_Size__c',
                                        'LeadsProfiler__Company_Size_ref__c',
                                        'LeadsProfiler__Country__c',
                                        'LeadsProfiler__Country_ref__c',
                                        'LeadsProfiler__DataObject__c',
                                        'LeadsProfiler__OriginalRank__c',
                                        'LeadsProfiler__OriginalRank_ref__c',
                                        'LeadsProfiler__Probability_Delta__c',
                                        'LeadsProfiler__Probability_Delta_ref__c',
                                        'LeadsProfiler__SalesPredict_Last_Update__c',
                                        'LeadsProfiler__SalesPredict_Last_Update_ref__c',
                                        'LeadsProfiler__SalesPredict_Rank__c',
                                        'LeadsProfiler__SalesPredict_report_rank__c',
                                        'LeadsProfiler__SalesPredict_report_rank_ref__c',
                                        'LeadsProfiler__Score__c',
                                        'LeadsProfiler__Score_ref__c',
                                        'LeadsProfiler__Solution_Fit__c',
                                        'LeadsProfiler__Solution_Fit_ref__c',
                                        'LeadsProfiler__State__c',
                                        'LeadsProfiler__State_ref__c',
                                        'LeadsProfiler__Street__c',
                                        'LeadsProfiler__Street_ref__c',
                                        'LeadsProfiler__Title__c',
                                        'LeadsProfiler__Title_ref__c',
                                        'LeadsProfiler__Vertical__c',
                                        'LeadsProfiler__Vertical_ref__c',
                                        'LeadsProfiler__Business_Group__c_account',
                                        'LeadsProfiler__Business_Group_ref__c_account',
                                        'LeadsProfiler__Buyer_Persona__c_account',
                                        'LeadsProfiler__Buyer_Persona_ref__c_account',
                                        'LeadsProfiler__ChangeRankReason__c_account',
                                        'LeadsProfiler__City__c_account',
                                        'LeadsProfiler__City_ref__c_account',
                                        'LeadsProfiler__Company_Profile__c_account',
                                        'LeadsProfiler__Company_Profile_ref__c_account',
                                        'LeadsProfiler__Company_Revenue__c_account',
                                        'LeadsProfiler__Company_Revenue_ref__c_account',
                                        'LeadsProfiler__Company_Size__c_account',
                                        'LeadsProfiler__Company_Size_ref__c_account',
                                        'LeadsProfiler__Country__c_account',
                                        'LeadsProfiler__Country_ref__c_account',
                                        'LeadsProfiler__DataObject__c_account',
                                        'LeadsProfiler__OriginalRank__c_account',
                                        'LeadsProfiler__OriginalRank_ref__c_account',
                                        'LeadsProfiler__Probability_Delta__c_account',
                                        'LeadsProfiler__Probability_Delta_ref__c_account',
                                        'LeadsProfiler__Renewal_Probability_Delta__c',
                                        'LeadsProfiler__Renewal_Probability_Delta_ref__c',
                                        'LeadsProfiler__Renewal_Score__c',
                                        'LeadsProfiler__Renewal_Score_ref__c',
                                        'LeadsProfiler__SalesPredict_Renewal_Rank__c',
                                        'LeadsProfiler__SalesPredict_Renewal_report_rank__c',
                                        'LeadsProfiler__SalesPredict_Renewal_report_rank_ref__c',
                                        'LeadsProfiler__SalesPredict_rank__c_account',
                                        'LeadsProfiler__SalesPredict_report_rank__c_account',
                                        'LeadsProfiler__SalesPredict_report_rank_ref__c_account',
                                        'LeadsProfiler__Score__c_account',
                                        'LeadsProfiler__Score_ref__c_account',
                                        'LeadsProfiler__Solution_Fit__c_account',
                                        'LeadsProfiler__Solution_Fit_ref__c_account',
                                        'LeadsProfiler__State__c_account',
                                        'LeadsProfiler__State_ref__c_account',
                                        'LeadsProfiler__Street__c_account',
                                        'LeadsProfiler__Street_ref__c_account',
                                        'LeadsProfiler__Title__c_account',
                                        'LeadsProfiler__Title_ref__c_account',
                                        'LeadsProfiler__Vertical__c_account',
                                        'LeadsProfiler__Vertical_ref__c_account',
                                        'LeadsProfiler__OriginalRank__c_contact',
                                        'LeadsProfiler__Score__c_contact',
                                        'Best_Service_LevelOn__c',
                                        'Total_Gold_License__c',
                                        'Total_Mission_Critical__c',
                                        'Total_Platinum_License__c',
                                        'iKOCompanyName',
                                        'iKOCompanyPhone',
                                        'iKOCompanySize',
                                        'iKOCompanyWebsite',
                                        'iKOCountry',
                                        'iKOEmailMain',
                                        'iKOFirstName',
                                        'iKOInsertTime',
                                        'iKOJobCategory',
                                        'iKOJobTitle',
                                        'iKOLastName',
                                        'iKOLeadIndustry',
                                        'iKOLeadOwner',
                                        'iKOLeadPhone',
                                        'Interest_DP__c',
                                        'campaign_creative',
                                        'Opp_Created_After_Added_to_Conversica__c',
                                        'Is_Current_License_Expired__c',
                                        'successfactors_id__c',
                                        'successfactors_id__c_contact',
                                        'Website_behavior_summary__c',
                                        'HW__c',
                                        'MapR__c',
                                        'Teradata_EDW_Teradata_TDH_Teradata__c',
                                        'AWS_AWS_Redshift_AWS_EMR_AWS_spar__c',
                                        'Google_Google_BigQuery_Google_DataP__c',
                                        'HP_Vertica__c',
                                        'MongoDB__c',
                                        'DataStax__c',
                                        'Tableau__c',
                                        'Couchbase__c',
                                        'Qlik__c',
                                        'CDH__c',
                                        'NS_Transaction_Customer__c',
                                        'CSM_Team_Manager__c',
                                        'Customer_One_Drive_Location__c',
                                        'Do_not_allow_super_users__c',
                                        'Gainsight_C360__c',
                                        #'tic_username',
                                        'Date_of_1st_Renewal_Sale__c',
                                        'Lead_Source_2__c',
                                        'mktoLeadOwnerFirstName',
                                        'mktoLeadOwnerLastName',
                                        'mktoLeadOwnerEmailAddress',
                                        'mktoLeadOwnerPhoneNumber',
                                        'mktoLeadOwnerFullname',
                                        'SalesPredict_AWS__c',
                                        'Legacy_User__c',
                                        'SD_Company_Name__c',
                                        'Preferred_Language__c',
                                        'Top_Priority__c',
                                        'Top_Customer__c',
                                        'SDR__c',
                                        'behavior_Score_at_MQL',
                                        'predictive_Rank_at_MQL',
                                        'lead_Score_at_MQL',
                                        'SalesPredict_Score_at_MQL',
                                        'sSMatched',
                                        'sSNotMatched',
                                        'Contact_License_Mismatch__c',
                                        'SDR_Email__c',
                                        'Converted_to_Opportunity__c',
                                        'Contact_License_Mismatch_reseller__c',
                                        'Converted_to_ContactC__c',
                                        'X1_Inquiry_date__c',
                                        'X2_Ready_for_Review_Date__c',
                                        'X3_Working_Date__c',
                                        'X4_Qualifying_Date__c',
                                        'X5_Qualified_Date__c',
                                        'X6_Recycle_Date__c',
                                        'X7_Do_Not_Contact_Date__c',
                                        'Acquisition_Asset_Type__c',
                                        'Acquisition_Campaign__c',
                                        'MQL_Asset_Type__c',
                                        'MQL_Campaign__c',
                                        'End_User_Contact__c',
                                        'Decision_Maker_Contact__c',
                                        'Linked_Account__c',
                                        'LeanData__A2B_Account__c',
                                        'LeanData__A2B_Group__c',
                                        'LeanData__Has_Matched__c',
                                        'LeanData__Marketing_Sys_Created_Date__c',
                                        'LeanData__Matched_Account_Annual_Revenue__c',
                                        'LeanData__Matched_Account_Billing_Country__c',
                                        'LeanData__Matched_Account_Billing_Postal_Code__c',
                                        'LeanData__Matched_Account_Billing_State__c',
                                        'LeanData__Matched_Account_Custom_Field_1__c',
                                        'LeanData__Matched_Account_Employees__c',
                                        'LeanData__Matched_Account_Industry__c',
                                        'LeanData__Matched_Account_Name__c',
                                        'LeanData__Matched_Account_Type__c',
                                        'LeanData__Matched_Account_Website__c',
                                        'LeanData__Matched_Account__c',
                                        'LeanData__Matched_Buyer_Persona__c',
                                        'LeanData__Matched_Lead__c',
                                        'LeanData__Reporting_Matched_Account__c',
                                        'LeanData__Reporting_Timestamp__c',
                                        'LeanData__Router_Status__c',
                                        'LeanData__Routing_Action__c',
                                        'LeanData__Routing_Status__c',
                                        'LeanData__Salesforce_Id__c',
                                        'LeanData__Search_Index__c',
                                        'LeanData__Search__c',
                                        'LeanData__Segment__c',
                                        'LeanData__Status_Info__c',
                                        'LeanData__Tag__c',
                                        'LeanData__LD_EmailDomain__c',
                                        'LeanData__LD_EmailDomains__c',
                                        'LeanData__Reporting_Customer__c',
                                        'LeanData__Reporting_Has_Opportunity__c',
                                        'LeanData__Reporting_Last_Marketing_Touch_Date__c',
                                        'LeanData__Reporting_Last_Sales_Touch_Date__c',
                                        'LeanData__Reporting_Recent_Marketing_Touches__c',
                                        'LeanData__Reporting_Target_Account_Number__c',
                                        'LeanData__Reporting_Target_Account__c',
                                        'LeanData__Reporting_Total_Leads_and_Contacts__c',
                                        'LeanData__Reporting_Total_Marketing_Touches__c',
                                        'LeanData__SLA__c',
                                        'LeanData__Scenario_1_Owner__c',
                                        'LeanData__Scenario_2_Owner__c',
                                        'LeanData__Scenario_3_Owner__c',
                                        'LeanData__Scenario_4_Owner__c',
                                        'LeanData__Search__c_account',
                                        'LeanData__Tag__c_account',
                                        'Convert_to_Contact__c',
                                        'BigDataSandbox',
                                        'DSCORGPKG__CUSTOM_COUNTRY__c',
                                        'DSCORGPKG__CUSTOM_STATE__c',
                                        'DSCORGPKG__Custom_Annual_Rev__c',
                                        'DSCORGPKG__Custom_Company_HQ__c',
                                        'DSCORGPKG__Custom_Emp_No__c',
                                        'DSCORGPKG__Custom_Fiscal_Year__c',
                                        'DSCORGPKG__Custom_ITBudget__c',
                                        'DSCORGPKG__Custom_ITEmp_c__c',
                                        'DSCORGPKG__Custom_LinkedUrl__c',
                                        'DSCORGPKG__Custom_Title__c',
                                        'DSCORGPKG__Locked_By_User__c',
                                        'DSCORGPKG__Cust_Fiscal_Year__c',
                                        'DSCORGPKG__Cust_IT_Budget__c',
                                        'DSCORGPKG__Custom_3yr__c',
                                        'DSCORGPKG__Custom_Country_Full_RA__c',
                                        'DSCORGPKG__Custom_Country_RA__c',
                                        'DSCORGPKG__Custom_DUNS__c',
                                        'DSCORGPKG__Custom_Emp_No__c_account',
                                        'DSCORGPKG__Custom_ITEmp__c',
                                        'DSCORGPKG__Custom_NOA__c',
                                        'DSCORGPKG__Custom_Revenue__c',
                                        'DSCORGPKG__Custom_State_Full_RA__c',
                                        'DSCORGPKG__Custom_State_RA__c',
                                        'DSCORGPKG__Custom_des__c',
                                        'DSCORGPKG__Locked_By_User__c_account',
                                        'DSCORGPKG__Custom_Address__c',
                                        'DSCORGPKG__Custom_Company_HQ_Address__c',
                                        'DSCORGPKG__Custom_Company_HQ_City__c',
                                        'DSCORGPKG__Custom_Country__c_contact',
                                        'DSCORGPKG__Custom_Phone__c',
                                        'DSCORGPKG__Custom_State__c_contact',
                                        'DSCORGPKG__REMOVELinkedinURL__c',
                                        'DSCORGPKG__title_Custom__c',
                                        'Talend_6_x__c',
                                        'Puchase_Influence_Level__c',
                                        'Author__c',
                                        'Survey_Language_Code__c',
                                        'CSM_User__c',
                                        'Current_Product_Version__c',
                                        'Follow_up_Escalation_Owner_1__c',
                                        'Market__c',
                                        'Product_Name__c',
                                        'Professional_Services__c',
                                        'Software_Upgrade__c',
                                        'Future_Theater__c',
                                        'Survey_Language_Code__c_contact',
                                        'Renewal_Check__c',
                                        'NPS_Check__c',
                                        'Purchase_Influence_Level__c',
                                        'Check__c',
                                        'Response_Rate_Notification_Recipient__c',
                                        'PrimaryScore__c',
                                        'AVA__AVAAI_action_required__c',
                                        'AVA__AVAAI_action_required_date__c',
                                        'AVA__AVAAI_conversation_stage__c',
                                        'AVA__AVAAI_conversation_stage_date__c',
                                        'AVA__AVAAI_conversation_status__c',
                                        'AVA__AVAAI_conversation_status_date__c',
                                        'AVA__AVAAI_conversica_lead_status__c',
                                        'AVA__AVAAI_conversica_lead_status_date__c',
                                        'cas__FirstAttempt__c',
                                        'cas__First_Conversation_Date__c',
                                        'cas__LastAttempt__c',
                                        'cas__Last_Connect__c',
                                        'cas__List_Name__c',
                                        'cas__Most_Recent_Attempt_Disposition__c',
                                        'cas__Most_Recent_Conversation_Disposition__c',
                                        'cas__Most_Recent_Disposition__c',
                                        'cas__NumberAttempts__c',
                                        'cas__NumberConnects__c',
                                        'cas__Penalty_Box_Status__c',
                                        'cas__ContactStatus__c',
                                        'Author_for_Opportunity__c',
                                        'NS_Account_Number__c',
                                        'Partner_portal_sourced__c',
                                        'Partner_portal_sourced__c_account',
                                        'Ctvt_CloseDate__c',
                                        'PartnerPortalSourced__c',
                                        'Lattice_Score__c',
                                        'Lattice_Timestamp__c',
                                        'Lattice_Webhook_Timestamp__c',
                                        'Ctvt_PartnerOrgName__c',
                                        'Ctvt_PartnerUserEmail__c',
                                        'Ctvt_CurrencyOfTheOpportunity_1_1__c',
                                        'Ctvt_Amount__c',
                                        'Ctvt_RegistrationStatus_1__c',
                                        'Ctvt_PartnerUserName__c',
                                        'Ctvt_Stage__c',
                                        'Ctvt_Title__c',
                                        'Ctvt_ProjectBudgetInLocalCurrency_1__c',
                                        'Ctvt_PartnerUserPhone__c',
                                        'Ctvt_TimelineOtherDatesAndDeadlines_1__c',
                                        'Ctvt_SummaryOfTheTechnicalEnvironme_1__c',
                                        'Ctvt_Sys_EntityType__c',
                                        'Ctvt_Sys_URL__c',
                                        'Ctvt_HowCanTalendHelpYouWithYourCus_1__c',
                                        'Ctvt_Sys_LastUpdated__c',
                                        'Ctvt_CurrentEngagementWithTheCustom_1__c',
                                        'Ctvt_EngagementHistoryWithTheCustom_1__c',
                                        'Ctvt_AnyOtherInformation_1__c',
                                        'Ctvt_SummaryOfTheDealopportunityKey_1__c',
                                        'Ctvt_DidYouTalkToATalendRepIfSoPlea_1__c',
                                        'LBI__EstimatedRevenue__c',
                                        'LBI__LatticeRating__c',
                                        'LBI__Recommendation__c',
                                        'LBI__AccountExtension__c',
                                        'LBI__NumberOfOpenInProgressRecommendations__c',
                                        'LBI__AccountName__c',
                                        'Lattice_Rank__c',
                                        'jobFunction2',
                                        'Critical_Account__c',
                                        'NPS_Check_Accts_up_for_Renewal__c',
                                        'Quarter__c',
                                        'Today_s_Quarter__c',
                                        'cventJobTitle',
                                        'cventAdmissionItem',
                                        'cventRegistrationType',
                                        'cventRegistrationStatus',
                                        'cventConfirmation',
                                        'cventRegistrationDate',
                                        'Ctvt_Description_1__c',
                                        'Ctvt_AnyOtherInformation_2__c',
                                        'Sales_Activities_Since_Last_MQL__c',
                                        'Latitude',
                                        'Longitude',
                                        'GeocodeAccuracy',
                                        'Address',
                                        'PhotoUrl',
                                        'LastViewedDate',
                                        'LastReferencedDate',
                                        'JigsawContactId_lead',
                                        'CleanStatus',
                                        'CompanyDunsNumber',
                                        'BillingLatitude',
                                        'BillingLongitude',
                                        'BillingGeocodeAccuracy',
                                        'BillingAddress',
                                        'ShippingLatitude',
                                        'ShippingLongitude',
                                        'ShippingGeocodeAccuracy',
                                        'ShippingAddress',
                                        'PhotoUrl_account',
                                        'LastViewedDate_account',
                                        'LastReferencedDate_account',
                                        'JigsawCompanyId_account',
                                        'CleanStatus_account',
                                        'AccountSource',
                                        'DunsNumber',
                                        'Tradestyle',
                                        'NaicsCode',
                                        'NaicsDesc',
                                        'YearStarted',
                                        'SicDesc',
                                        'OtherLatitude',
                                        'OtherLongitude',
                                        'OtherGeocodeAccuracy',
                                        'OtherAddress',
                                        'MailingLatitude',
                                        'MailingLongitude',
                                        'MailingGeocodeAccuracy',
                                        'MailingAddress',
                                        'IsEmailBounced',
                                        'Ctvt_AdditionalInformation_1__c',
                                        'Ctvt_HowCanTalendAssistYouWithYourC__c',
                                        'LIM_since_Recycle__c',
                                        'leadCodeCustom',
                                        'First_Activity__c',
                                        'Lattice_Behavioral_Score__c',
                                        'Lattice_Behavioral_Timestamp__c',
                                        'Lattice_Behavioral_Rating__c',
                                        'Assigned_CSMs__c',
                                        'Lattice_Fit_Behavior__c',
                                        'Lattice_Fit_Behavior_Timestamp__c',
                                        'Awareness_Campaign_Sent__c',
                                        'DP_included_in_on_boarding__c',
                                        'Info_Requested__c',
                                        'Demo_Requested__c',
                                        'POC_Requested__c',
                                        'Free_Licenses_activated__c',
                                        'DP_in_Prod_Use__c',
                                        'rrpu__Alert_Message__c',
                                        'rrpu__Alert_Message__c_account',
                                        'LPI_Cloud_Infrastructure_Tech__c',
                                        'LPI_Cloud_Service_Tier_1__c',
                                        'LPI_Cloud_Service_Tier_2__c',
                                        'LBI_Cloud_Infrastructure_Tech__c',
                                        'LBI_Cloud_Service_Tier_1__c',
                                        'LBI_Cloud_Service_Tier_2__c',
                                        'LPI_Has_Adobe_Target_Standard__c',
                                        'LPI_Has_Amazon_AWS__c',
                                        'LBI_Has_Amazon_Redshift__c',
                                        'LPI_Has_Apache_Hadoop__c',
                                        'LBI_Has_Apache_Hive__c',
                                        'LBI_Has_Cloudera__c',
                                        'LBI_Has_CoolaData__c',
                                        'LBI_Has_IBM_InfoSphere_DataStage__c',
                                        'LBI_Has_Informatica__c',
                                        'LBI_Has_Loggly__c',
                                        'LBI_Has_Mulesoft__c',
                                        'LBI_Has_Rekko__c',
                                        'LBI_Has_TellApart__c',
                                        'LBI_Has_Adobe_Target_Standard__c',
                                        'LBI_Has_Amazon_AWS__c',
                                        'LBI_Has_Apache_Hadoop__c',
                                        'Express_Consent__c',
                                        'Express_Consent_History__c',
                                        'Inferred_Consent__c',
                                        'Inferred_Consent_History__c',
                                        'Created_By_Role__c',
                                        'Global_Account__c',
                                        'Regional_AE__c',
                                        'First_MQL_Date__c',
                                        'Not_Interested__c',
                                        'Date_of_Last_Data_Prep_Conversation__c',
                                        'Active_User_Status__c',
                                        'temp_assignment',
                                        'Ctvt_RenewalOpportunity__c',
                                        'Ctvt_BrandNewOpportunity__c',
                                        'Chat_Transcript__c',
                                        'Chat_Agent_ID__c',
                                        'Payment_Term__c',
                                        'Customer_Acquisition_Date__c',
                                        'Account_ID_long__c',
                                        'LMS_Student_ID__c',
                                        'Actual_Users__c',
                                        'Are_you_using_Joblets__c',
                                        'Big_Data_Components__c',
                                        'Big_Data_Streaming_in_Use__c',
                                        'Building_Actions__c',
                                        'Building_Map_Reduce_of_Spark_Batch_Jobs__c',
                                        'Building_Mediation_Routes__c',
                                        'Building_SOAP_or_REST_Services__c',
                                        'Building_a_Lambda_Kappa_Zeta_Arch__c',
                                        'Cloud_Environment__c',
                                        'Completed_Training__c',
                                        'DEV__c',
                                        'Data_Cleansing_Masking_Used__c',
                                        'Database_Type__c',
                                        'Develop_Using_Spring_DLS__c',
                                        'Disaster_Recovery__c',
                                        'EOL_12_months__c',
                                        'Engaged__c',
                                        'Finite_Project__c',
                                        'Hadoop_Components_Used__c',
                                        'How_many_data_stewards__c',
                                        'Implementation_Approach__c',
                                        'Implementation__c',
                                        'In_Production__c',
                                        'Java_Version__c',
                                        'MDMs_Driving_Critical_Business_Processes__c',
                                        'Open_Feature_Request__c',
                                        'Operating_System__c',
                                        'Pre_Production__c',
                                        'Product_Deployed_in_the_Cloud__c',
                                        'Production__c',
                                        'Referenceable__c',
                                        'System_Integration_Test__c',
                                        'TAC_Users__c',
                                        'TEST__c',
                                        'User_Acceptance_Test__c',
                                        'Using_All_Licenses__c',
                                        'Using_All_Products__c',
                                        'Using_Big_Data_Components__c',
                                        'Using_ML_Algorithms_or_Components__c',
                                        'Using_Metadata_Bridge__c',
                                        'Using_Profiling_features_of_the_Studio__c',
                                        'Using_Spark_Streaming__c',
                                        'Using_TAC_in_Development__c',
                                        'Using_TAC_in_High_Availability__c',
                                        'Using_TAC_in_Production__c',
                                        'Using_Talend_Data_Mapper__c',
                                        'Using_Talend_Data_Prep_2_Free_Licenses__c',
                                        'Using_Virtual_Servers_Groups__c',
                                        'Version__c',
                                        'of_Dev_Ops_Admin_Ops_Users__c',
                                        'of_Environments__c',
                                        'of_Studio_Users__c',
                                        'of_Testers__c',
                                        'Usage_Rate__c',
                                        'Customer_Success_SharePoint_Search__c',
                                        'personTimeZone',
                                        'Account_Discount__c',
                                        'Account_Services_Discount__c',
                                        'AVA_SFCPQ__ExemptEntityType__c',
                                        'AVA_SFCPQ__TaxExemptionCode__c',
                                        'Account_Has_Cust_Terms__c',
                                        'tICDataCenterLocation',
                                        'tICAcceptTerms',
                                        'dataLakeAccelerator',
                                        'Remove_Account__c',
                                        'Acct_Revenue_MAX__c',
                                        'Total_Opps_Stage_2__c',
                                        'Partner_Status__c',
                                        'Premier_Partner__c',
                                        'Partner_Level__c',
                                        'Lead__c',
                                        'Account__c',
                                        'Dietary_Requirements',
                                        'qbdialer__Related_Contact_Dials__c',
                                        'qbdialer__Related_Contact_LastCallTime__c',
                                        'Primary_Partner_Level__c',
                                        'Primary_Partner_Owner__c',
                                        'Primary_Partner_Type__c',
                                        'Primary_Premier_Partner__c',
                                        'Sourcing_Partner__c',
                                        'MQL_Date_Time_Last__c',
                                        'bTLKLevel',
                                        'bTLKUserID',
                                        'bTLKLeadContext',
                                        'bTLKLeadType',
                                        'bTLKReferral',
                                        'bTLKChannelID',
                                        'bTLKChannelName',
                                        'bTLKChannelOrganization',
                                        'bTLKChannelsBrightTALKURL',
                                        'bTLKEngagementScore',
                                        'bTLKTimeZone',
                                        'bTLKEmbedMarketoToken',
                                        'bTLKEmbedURL',
                                        'bTLKEmbedUTMSource',
                                        'bTLKEmbedUTMTerm',
                                        'bTLKEmbedUTMMedium',
                                        'bTLKEmbedUTMContent',
                                        'bTLKEmbedUTMCampaign',
                                        'bTLKActivityType',
                                        'bTLKWebcastID',
                                        'bTLKWebcastURL',
                                        'bTLKWebcastTitle',
                                        'bTLKLastActivityDate',
                                        'bTLKLiveMinutesViewed',
                                        'bTLKRecordedMinutesViewed',
                                        'bTLKTotalMinutesViewed',
                                        'bTLKViewingURL',
                                        'bTLKUTMSource',
                                        'bTLKUTMTerm',
                                        'bTLKUTMMedium',
                                        'bTLKUTMContent',
                                        'bTLKUTMCampaign',
                                        'bTLKWebcastPresenter',
                                        'bTLKWebcastDuration',
                                        'bTLKWebcastDurationMinutes',
                                        'bTLKCreatedDate',
                                        'bTLKPreregistered',
                                        'bTLKLiveViewingDuration',
                                        'bTLKLiveViewingsCount',
                                        'bTLKRecordedViewingDuration',
                                        'bTLKRecordedViewingsCount',
                                        'bTLKTotalViewingDuration',
                                        'bTLKTotalViewingsCount',
                                        'bTLKMarketoToken',
                                        'bTLKAttachmentID',
                                        'bTLKAttachmentTitle',
                                        'bTLKAttachmentType',
                                        'bTLKAttachmentURL',
                                        'bTLKFirstAccessedDate',
                                        'bTLKAttachmentActivityID',
                                        'bTLKLastAccessedDate',
                                        'bTLKLiveViewAccessCount',
                                        'bTLKRecordedAccessCount',
                                        'bTLKTotalAccessCount',
                                        'bTLKLastAccessURL',
                                        'bTLKLastAccessMarketoToken',
                                        'bTLKLastAccessUTMCampaign',
                                        'bTLKLastAccessUTMContent',
                                        'bTLKLastAccessUTMMedium',
                                        'bTLKLastAccessUTMSource',
                                        'bTLKLastAccessUTMTerm',
                                        'First_Activity_Time__c',
                                        'Total_Activities_Including_Outreach_Dia__c',
                                        'Total_Activities_MQL_With_Outreach__c',
                                        'Total_Number_of_Activities__c',
                                        'Total_Number_of_Activities_since_MQL__c',
                                        'ddc_prospector__Sourced_from_Data_com__c',
                                        'ddc_prospector__Sourced_from_Data_com__c_account',
                                        'ddc_prospector__Sourced_from_Data_com__c_contact',
                                        'Contacts_Previous_Experience__c',
                                        'Secondary_Account_Revenue__c',
                                        'Secondary_Account_Revenue_Source__c',
                                        'Contact_ID_long__c',
                                        'Resource_URL',
                                        'Resource_Name',
                                        'Resource_ID',
                                        'Account_Segment_CFY__c',
                                        'Is_Domestic_Parent__c',
                                        'Domestic_Parent__c'])

        for index, item in enumerate(leads):
            ##if int(item["id"]) > 515752:
            b=1
            records1.set_value(index, 'company', str(item["company"]))
            records1.set_value(index, 'site', str(item["site"]))
            records1.set_value(index, 'street', str(item["street"]))
            records1.set_value(index, 'city', str(item["city"]))
            records1.set_value(index, 'state', str(item["state"]))
            records1.set_value(index, 'country', str(item["country"]))
            records1.set_value(index, 'postalCode', str(item["postalCode"]))
            records1.set_value(index, 'website', str(item["website"]))
            records1.set_value(index, 'mainPhone', str(item["mainPhone"]))
            records1.set_value(index, 'annualRevenue', str(item["annualRevenue"]))
            records1.set_value(index, 'numberOfEmployees', str(item["numberOfEmployees"]))
            records1.set_value(index, 'industry', str(item["industry"]))
            records1.set_value(index, 'sicCode', str(item["sicCode"]))
            records1.set_value(index, 'mktoCompanyNotes', str(item["mktoCompanyNotes"]))
            records1.set_value(index, 'sfdcAccountId', str(item["sfdcAccountId"]))
            records1.set_value(index, 'id', str(item["id"]))
            records1.set_value(index, 'mktoName', str(item["mktoName"]))
            records1.set_value(index, 'personType', str(item["personType"]))
            records1.set_value(index, 'mktoIsPartner', str(item["mktoIsPartner"]))
            records1.set_value(index, 'isLead', str(item["isLead"]))
            records1.set_value(index, 'mktoIsCustomer', str(item["mktoIsCustomer"]))
            records1.set_value(index, 'isAnonymous', str(item["isAnonymous"]))
            records1.set_value(index, 'salutation', str(item["salutation"]))
            records1.set_value(index, 'firstName', str(item["firstName"]))
            records1.set_value(index, 'middleName', str(item["middleName"]))
            records1.set_value(index, 'lastName', str(item["lastName"]))
            records1.set_value(index, 'email', str(item["email"]))
            records1.set_value(index, 'phone', str(item["phone"]))
            records1.set_value(index, 'mobilePhone', str(item["mobilePhone"]))
            records1.set_value(index, 'fax', str(item["fax"]))
            records1.set_value(index, 'title', str(item["title"]))
            records1.set_value(index, 'contactCompany', str(item["contactCompany"]))
            records1.set_value(index, 'dateOfBirth', str(item["dateOfBirth"]))
            records1.set_value(index, 'personPrimaryLeadInterest', str(item["personPrimaryLeadInterest"]))
            records1.set_value(index, 'originalSourceType', str(item["originalSourceType"]))
            records1.set_value(index, 'originalSourceInfo', str(item["originalSourceInfo"]))
            records1.set_value(index, 'registrationSourceType', str(item["registrationSourceType"]))
            records1.set_value(index, 'registrationSourceInfo', str(item["registrationSourceInfo"]))
            records1.set_value(index, 'originalSearchEngine', str(item["originalSearchEngine"]))
            records1.set_value(index, 'originalSearchPhrase', str(item["originalSearchPhrase"]))
            records1.set_value(index, 'originalReferrer', str(item["originalReferrer"]))
            records1.set_value(index, 'emailInvalid', str(item["emailInvalid"]))
            records1.set_value(index, 'emailInvalidCause', str(item["emailInvalidCause"]))
            records1.set_value(index, 'unsubscribed', str(item["unsubscribed"]))
            records1.set_value(index, 'unsubscribedReason', str(item["unsubscribedReason"]))
            records1.set_value(index, 'doNotCall', str(item["doNotCall"]))
            records1.set_value(index, 'mktoDoNotCallCause', str(item["mktoDoNotCallCause"]))
            records1.set_value(index, 'doNotCallReason', str(item["doNotCallReason"]))
            records1.set_value(index, 'mktoPersonNotes', str(item["mktoPersonNotes"]))
            records1.set_value(index, 'sfdcType', str(item["sfdcType"]))
            records1.set_value(index, 'sfdcContactId', str(item["sfdcContactId"]))
            records1.set_value(index, 'anonymousIP', str(item["anonymousIP"]))
            records1.set_value(index, 'inferredCompany', str(item["inferredCompany"]))
            records1.set_value(index, 'inferredCountry', str(item["inferredCountry"]))
            records1.set_value(index, 'inferredCity', str(item["inferredCity"]))
            records1.set_value(index, 'inferredStateRegion', str(item["inferredStateRegion"]))
            records1.set_value(index, 'inferredPostalCode', str(item["inferredPostalCode"]))
            records1.set_value(index, 'inferredMetropolitanArea', str(item["inferredMetropolitanArea"]))
            records1.set_value(index, 'inferredPhoneAreaCode', str(item["inferredPhoneAreaCode"]))
            records1.set_value(index, 'createdAt', str(item["createdAt"]))
            records1.set_value(index, 'updatedAt', str(item["updatedAt"]))
            records1.set_value(index, 'leadPerson', str(item["leadPerson"]))
            records1.set_value(index, 'leadRole', str(item["leadRole"]))
            records1.set_value(index, 'leadSource', str(item["leadSource"]))
            records1.set_value(index, 'leadStatus', str(item["leadStatus"]))
            records1.set_value(index, 'leadScore', str(item["leadScore"]))
            records1.set_value(index, 'urgency', str(item["urgency"]))
            records1.set_value(index, 'priority', str(item["priority"]))
            records1.set_value(index, 'relativeScore', str(item["relativeScore"]))
            records1.set_value(index, 'relativeUrgency', str(item["relativeUrgency"]))
            records1.set_value(index, 'rating', str(item["rating"]))
            records1.set_value(index, 'sfdcLeadId', str(item["sfdcLeadId"]))
            records1.set_value(index, 'sfdcLeadOwnerId', str(item["sfdcLeadOwnerId"]))
            records1.set_value(index, 'leadPartitionId', str(item["leadPartitionId"]))
            records1.set_value(index, 'leadRevenueCycleModelId', str(item["leadRevenueCycleModelId"]))
            records1.set_value(index, 'leadRevenueStageId', str(item["leadRevenueStageId"]))
            records1.set_value(index, 'Interest_DI', str(item["Interest_DI"]))
            records1.set_value(index, 'Interest_DQ', str(item["Interest_DQ"]))
            records1.set_value(index, 'Interest_MDM', str(item["Interest_MDM"]))
            records1.set_value(index, 'Interest_ESB', str(item["Interest_ESB"]))
            records1.set_value(index, 'Sugar_lead_id', str(item["Sugar_lead_id"]))
            records1.set_value(index, 'Sugar_cid', str(item["Sugar_cid"]))
            records1.set_value(index, 'Business_zone', str(item["Business_zone"]))
            records1.set_value(index, 'Phone_office_valid', str(item["Phone_office_valid"]))
            records1.set_value(index, 'Phone_mobile_valid', str(item["Phone_mobile_valid"]))
            records1.set_value(index, 'Language_preference', str(item["Language_preference"]))
            records1.set_value(index, 'Phone_extension', str(item["Phone_extension"]))
            records1.set_value(index, 'Department', str(item["Department"]))
            records1.set_value(index, 'Status_in_CRM', str(item["Status_in_CRM"]))
            records1.set_value(index, 'BDR_interest_determination', str(item["BDR_interest_determination"]))
            records1.set_value(index, 'Bounced_elsewhere', str(item["Bounced_elsewhere"]))
            records1.set_value(index, 'Account_potential', str(item["Account_potential"]))
            records1.set_value(index, 'acquisitionProgramId', str(item["acquisitionProgramId"]))
            records1.set_value(index, 'mktoAcquisitionDate', str(item["mktoAcquisitionDate"]))
            records1.set_value(index, 'Test', str(item["Test"]))
            records1.set_value(index, 'LastScoring-Adoption', str(item["LastScoring-Adoption"]))
            records1.set_value(index, 'jigsawContactStatus', str(item["jigsawContactStatus"]))
            records1.set_value(index, 'jigsawContactId', str(item["jigsawContactId"]))
            records1.set_value(index, 'sfdcId', str(item["sfdcId"]))
            records1.set_value(index, 'Interest_TIF', str(item["Interest_TIF"]))
            records1.set_value(index, 'Interest_TFS', str(item["Interest_TFS"]))
            records1.set_value(index, 'LastInteractionDate', str(item["LastInteractionDate"]))
            records1.set_value(index, 'JobFunction', str(item["JobFunction"]))
            records1.set_value(index, 'PrimaryProductInterest', str(item["PrimaryProductInterest"]))
            records1.set_value(index, 'LeadComments', str(item["LeadComments"]))
            records1.set_value(index, 'SalesAlert', str(item["SalesAlert"]))
            records1.set_value(index, 'Alert', str(item["Alert"]))
            records1.set_value(index, 'Third-PartySource', str(item["Third-PartySource"]))
            records1.set_value(index, 'Marketo_SFDC_Id', str(item["Marketo_SFDC_Id"]))
            records1.set_value(index, 'NetSuiteId', str(item["NetSuiteId"]))
            records1.set_value(index, 'SendtoNetsuite', str(item["SendtoNetsuite"]))
            records1.set_value(index, 'Push_to_Sales', str(item["Push_to_Sales"]))
            records1.set_value(index, 'NS_Email', str(item["NS_Email"]))
            records1.set_value(index, 'AccountType', str(item["AccountType"]))
            records1.set_value(index, 'Territory', str(item["Territory"]))
            records1.set_value(index, 'Job_Level', str(item["Job_Level"]))
            records1.set_value(index, 'Use_Case', str(item["Use_Case"]))
            records1.set_value(index, 'Last_Scoring_UserDoc', str(item["Last_Scoring_UserDoc"]))
            records1.set_value(index, 'Last_Scoring_ProductReg', str(item["Last_Scoring_ProductReg"]))
            records1.set_value(index, 'Last_Scoring_Tutorial', str(item["Last_Scoring_Tutorial"]))
            records1.set_value(index, 'Adoption_Level', str(item["Adoption_Level"]))
            records1.set_value(index, 'jigsawCompanyStatus', str(item["jigsawCompanyStatus"]))
            records1.set_value(index, 'jigsawCompanyId', str(item["jigsawCompanyId"]))
            records1.set_value(index, 'Nurture_Campaign_Assigned', str(item["Nurture_Campaign_Assigned"]))
            records1.set_value(index, 'Alert_Date', str(item["Alert_Date"]))
            records1.set_value(index, 'Lead_Comment_History', str(item["Lead_Comment_History"]))
            records1.set_value(index, 'Indicated_Industry', str(item["Indicated_Industry"]))
            records1.set_value(index, 'SD_Company_Name', str(item["SD_Company_Name"]))
            records1.set_value(index, 'SD_Company_Address', str(item["SD_Company_Address"]))
            records1.set_value(index, 'SD_Company_State', str(item["SD_Company_State"]))
            records1.set_value(index, 'SD_Company_Postal_Code', str(item["SD_Company_Postal_Code"]))
            records1.set_value(index, 'SD_Company_Country', str(item["SD_Company_Country"]))
            records1.set_value(index, 'SD_Company_Phone', str(item["SD_Company_Phone"]))
            records1.set_value(index, 'SD_Source', str(item["SD_Source"]))
            records1.set_value(index, 'SD_ID', str(item["SD_ID"]))
            records1.set_value(index, 'SD_Date', str(item["SD_Date"]))
            records1.set_value(index, 'SD_Match_Confidence', str(item["SD_Match_Confidence"]))
            records1.set_value(index, 'SD_Company_Fax', str(item["SD_Company_Fax"]))
            records1.set_value(index, 'SD_Entity_Type', str(item["SD_Entity_Type"]))
            records1.set_value(index, 'SD_Business_Description', str(item["SD_Business_Description"]))
            records1.set_value(index, 'SD_Ultimate_Parent_ID', str(item["SD_Ultimate_Parent_ID"]))
            records1.set_value(index, 'SD_Ultimate_Parent_Name', str(item["SD_Ultimate_Parent_Name"]))
            records1.set_value(index, 'NAIC_Code', str(item["NAIC_Code"]))
            records1.set_value(index, 'SD_Revenue_Currency', str(item["SD_Revenue_Currency"]))
            records1.set_value(index, 'SD_Assets_USD', str(item["SD_Assets_USD"]))
            records1.set_value(index, 'SD_Company_Stock_Exchange', str(item["SD_Company_Stock_Exchange"]))
            records1.set_value(index, 'SD_Company_Ticker_Symbol', str(item["SD_Company_Ticker_Symbol"]))
            records1.set_value(index, 'SD_Number_Employees', str(item["SD_Number_Employees"]))
            records1.set_value(index, 'ProductVersion', str(item["ProductVersion"]))
            records1.set_value(index, 'Telemarketing_Status', str(item["Telemarketing_Status"]))
            records1.set_value(index, 'Interest_BPM', str(item["Interest_BPM"]))
            records1.set_value(index, 'Interest_BigData', str(item["Interest_BigData"]))
            records1.set_value(index, 'Phone_Invalid', str(item["Phone_Invalid"]))
            records1.set_value(index, 'PostalCode_Invalid', str(item["PostalCode_Invalid"]))
            records1.set_value(index, 'EmailInvalid_API', str(item["EmailInvalid_API"]))
            records1.set_value(index, 'CurrentNurtureProgram', str(item["CurrentNurtureProgram"]))
            records1.set_value(index, 'Asset', str(item["Asset"]))
            records1.set_value(index, 'Username', str(item["Username"]))
            records1.set_value(index, 'LeadSelf-Identifier', str(item["LeadSelf-Identifier"]))
            records1.set_value(index, 'RoadshowChoice1', str(item["RoadshowChoice1"]))
            records1.set_value(index, 'RoadshowChoice2', str(item["RoadshowChoice2"]))
            records1.set_value(index, 'Asset_History', str(item["Asset_History"]))
            records1.set_value(index, 'gender', str(item["gender"]))
            records1.set_value(index, 'facebookDisplayName', str(item["facebookDisplayName"]))
            records1.set_value(index, 'twitterDisplayName', str(item["twitterDisplayName"]))
            records1.set_value(index, 'linkedInDisplayName', str(item["linkedInDisplayName"]))
            records1.set_value(index, 'facebookProfileURL', str(item["facebookProfileURL"]))
            records1.set_value(index, 'twitterProfileURL', str(item["twitterProfileURL"]))
            records1.set_value(index, 'linkedInProfileURL', str(item["linkedInProfileURL"]))
            records1.set_value(index, 'facebookPhotoURL', str(item["facebookPhotoURL"]))
            records1.set_value(index, 'twitterPhotoURL', str(item["twitterPhotoURL"]))
            records1.set_value(index, 'linkedInPhotoURL', str(item["linkedInPhotoURL"]))
            records1.set_value(index, 'facebookReach', str(item["facebookReach"]))
            records1.set_value(index, 'twitterReach', str(item["twitterReach"]))
            records1.set_value(index, 'linkedInReach', str(item["linkedInReach"]))
            records1.set_value(index, 'facebookReferredVisits', str(item["facebookReferredVisits"]))
            records1.set_value(index, 'twitterReferredVisits', str(item["twitterReferredVisits"]))
            records1.set_value(index, 'linkedInReferredVisits', str(item["linkedInReferredVisits"]))
            records1.set_value(index, 'totalReferredVisits', str(item["totalReferredVisits"]))
            records1.set_value(index, 'facebookReferredEnrollments', str(item["facebookReferredEnrollments"]))
            records1.set_value(index, 'twitterReferredEnrollments', str(item["twitterReferredEnrollments"]))
            records1.set_value(index, 'linkedInReferredEnrollments', str(item["linkedInReferredEnrollments"]))
            records1.set_value(index, 'totalReferredEnrollments', str(item["totalReferredEnrollments"]))
            records1.set_value(index, 'lastReferredVisit', str(item["lastReferredVisit"]))
            records1.set_value(index, 'lastReferredEnrollment', str(item["lastReferredEnrollment"]))
            #records1.set_value(index, 'TalendEmployee', str(item["TalendEmployee"]))
            records1.set_value(index, 'TimeSlot', str(item["TimeSlot"]))
            records1.set_value(index, 'TimeSlot2', str(item["TimeSlot2"]))
            records1.set_value(index, 'syndicationId', str(item["syndicationId"]))
            records1.set_value(index, 'CampaignSource', str(item["CampaignSource"]))
            records1.set_value(index, 'CampaignMedium', str(item["CampaignMedium"]))
            records1.set_value(index, 'CampaignTerm', str(item["CampaignTerm"]))
            records1.set_value(index, 'CampaignID', str(item["CampaignID"]))
            records1.set_value(index, 'Registered_BD', str(item["Registered_BD"]))
            records1.set_value(index, 'Registered_ESB', str(item["Registered_ESB"]))
            records1.set_value(index, 'Registered_MDM', str(item["Registered_MDM"]))
            records1.set_value(index, 'Registered_DQ', str(item["Registered_DQ"]))
            records1.set_value(index, 'Registered_DI', str(item["Registered_DI"]))
            records1.set_value(index, 'CampaignContent', str(item["CampaignContent"]))
            records1.set_value(index, 'RegisteredProductName', str(item["RegisteredProductName"]))
            records1.set_value(index, 'ProductNameRecognized', str(item["ProductNameRecognized"]))
            records1.set_value(index, 'RegisteredProducts', str(item["RegisteredProducts"]))
            records1.set_value(index, 'RegisteredProductType', str(item["RegisteredProductType"]))
            records1.set_value(index, 'ForumNotes', str(item["ForumNotes"]))
            records1.set_value(index, 'RoadshowChoice3', str(item["RoadshowChoice3"]))
            records1.set_value(index, 'QualifiedUser', str(item["QualifiedUser"]))
            records1.set_value(index, 'LeadSourceDetail', str(item["LeadSourceDetail"]))
            records1.set_value(index, 'upgradeinterest', str(item["upgradeinterest"]))
            records1.set_value(index, 'facebookId', str(item["facebookId"]))
            records1.set_value(index, 'twitterId', str(item["twitterId"]))
            records1.set_value(index, 'linkedInId', str(item["linkedInId"]))
            records1.set_value(index, 'Rep_First_Name', str(item["Rep_First_Name"]))
            records1.set_value(index, 'Rep_Last_Name', str(item["Rep_Last_Name"]))
            records1.set_value(index, 'Rep_Email_Address', str(item["Rep_Email_Address"]))
            records1.set_value(index, 'Rep_Job_Title', str(item["Rep_Job_Title"]))
            records1.set_value(index, 'Behavior_Score', str(item["Behavior_Score"]))
            records1.set_value(index, 'Demographic_Score', str(item["Demographic_Score"]))
            records1.set_value(index, 'Product_Evaluation_Request', str(item["Product_Evaluation_Request"]))
            records1.set_value(index, 'Product_Evaluation_Request_History',
                               str(item["Product_Evaluation_Request_History"]))
            records1.set_value(index, 'Last_Product_Evaluation_Request_Date',
                               str(item["Last_Product_Evaluation_Request_Date"]))
            records1.set_value(index, 'Product_Evaluation_Request_Activity_Log',
                               str(item["Product_Evaluation_Request_Activity_Log"]))
            records1.set_value(index, 'TechTarget_AI_Contact_Link', str(item["TechTarget_AI_Contact_Link"]))
            records1.set_value(index, 'Nurture_Program_Changed', str(item["Nurture_Program_Changed"]))
            records1.set_value(index, 'Named_Account', str(item["Named_Account"]))
            records1.set_value(index, 'Rep_Phone_Number', str(item["Rep_Phone_Number"]))
            records1.set_value(index, 'nurture_campaign_flow_stop', str(item["nurture_campaign_flow_stop"]))
            records1.set_value(index, 'nurture_campaign_flow_start', str(item["nurture_campaign_flow_start"]))
            records1.set_value(index, 'sandboxInstance', str(item["sandboxInstance"]))
            records1.set_value(index, 'cookies', str(item["cookies"]))
            records1.set_value(index, 'CurrencyIsoCode', str(item["CurrencyIsoCode"]))
            records1.set_value(index, 'EmailBouncedReason', str(item["EmailBouncedReason"]))
            records1.set_value(index, 'EmailBouncedDate', str(item["EmailBouncedDate"]))
            records1.set_value(index, 'DSCORGPKG__DeletedFromDiscoverOrg__c',
                               str(item["DSCORGPKG__DeletedFromDiscoverOrg__c"]))
            records1.set_value(index, 'DSCORGPKG__DiscoverOrg_Company_ID__c',
                               str(item["DSCORGPKG__DiscoverOrg_Company_ID__c"]))
            records1.set_value(index, 'DSCORGPKG__DiscoverOrg_ID__c', str(item["DSCORGPKG__DiscoverOrg_ID__c"]))
            records1.set_value(index, 'DSCORGPKG__DiscoverOrg_Technologies__c',
                               str(item["DSCORGPKG__DiscoverOrg_Technologies__c"]))
            records1.set_value(index, 'DSCORGPKG__ITOrgChart__c', str(item["DSCORGPKG__ITOrgChart__c"]))
            records1.set_value(index, 'DSCORGPKG__LinkedIn_URL__c', str(item["DSCORGPKG__LinkedIn_URL__c"]))
            records1.set_value(index, 'DSCORGPKG__ReportsTo__c', str(item["DSCORGPKG__ReportsTo__c"]))
            records1.set_value(index, 'DSCORGPKG__Twitter_URL__c', str(item["DSCORGPKG__Twitter_URL__c"]))
            records1.set_value(index, 'Alert_Phone__c', str(item["Alert_Phone__c"]))
            records1.set_value(index, 'Competition__c', str(item["Competition__c"]))
            records1.set_value(index, 'Do_Not_Call_Reason__c', str(item["Do_Not_Call_Reason__c"]))
            records1.set_value(index, 'Function_called_Job_Function_in_Marketo__c',
                               str(item["Function_called_Job_Function_in_Marketo__c"]))
            records1.set_value(index, 'Job_Role__c', str(item["Job_Role__c"]))
            records1.set_value(index, 'LinkedIn_URL__c', str(item["LinkedIn_URL__c"]))
            records1.set_value(index, 'MQL_Channel__c', str(item["MQL_Channel__c"]))
            records1.set_value(index, 'MQL_Date__c', str(item["MQL_Date__c"]))
            records1.set_value(index, 'MQL_Program__c', str(item["MQL_Program__c"]))
            records1.set_value(index, 'Mobile_Phone__c', str(item["Mobile_Phone__c"]))
            records1.set_value(index, 'Notes_for_Marketing_Only__c', str(item["Notes_for_Marketing_Only__c"]))
            records1.set_value(index, 'Nurture_Return__c', str(item["Nurture_Return__c"]))
            records1.set_value(index, 'Other_Competition__c', str(item["Other_Competition__c"]))
            records1.set_value(index, 'Phone_Business__c', str(item["Phone_Business__c"]))
            records1.set_value(index, 'Phone_Extension_Business__c', str(item["Phone_Extension_Business__c"]))
            records1.set_value(index, 'Reason_Code__c', str(item["Reason_Code__c"]))
            records1.set_value(index, 'RegionF__c', str(item["RegionF__c"]))
            records1.set_value(index, 'Region__c', str(item["Region__c"]))
            records1.set_value(index, 'mkto_si__HideDate__c', str(item["mkto_si__HideDate__c"]))
            records1.set_value(index, 'mkto_si__MSIContactId__c', str(item["mkto_si__MSIContactId__c"]))
            records1.set_value(index, 'CurrencyIsoCode_account', str(item["CurrencyIsoCode_account"]))
            records1.set_value(index, 'Channel_tier__c_account', str(item["Channel_tier__c_account"]))
            records1.set_value(index, 'Customer_Type__c', str(item["Customer_Type__c"]))
            records1.set_value(index, 'Region__c_account', str(item["Region__c_account"]))
            records1.set_value(index, 'DSCORGPKG__DiscoverOrg_ID__c_account',
                               str(item["DSCORGPKG__DiscoverOrg_ID__c_account"]))
            records1.set_value(index, 'Account_Potential__c_account', str(item["Account_Potential__c_account"]))
            records1.set_value(index, 'Account_Subsidiary__c', str(item["Account_Subsidiary__c"]))
            records1.set_value(index, 'Competition__c_account', str(item["Competition__c_account"]))
            records1.set_value(index, 'Language__c', str(item["Language__c"]))
            records1.set_value(index, 'Other_Competition__c_account', str(item["Other_Competition__c_account"]))
            records1.set_value(index, 'CurrencyIsoCode_contact', str(item["CurrencyIsoCode_contact"]))
            records1.set_value(index, 'Alt_Email__c', str(item["Alt_Email__c"]))
            records1.set_value(index, 'Function__c', str(item["Function__c"]))
            records1.set_value(index, 'Use_Case__c_contact', str(item["Use_Case__c_contact"]))
            records1.set_value(index, 'mkto_si__Sales_Insight__c', str(item["mkto_si__Sales_Insight__c"]))
            records1.set_value(index, 'lastProgramChannel', str(item["lastProgramChannel"]))
            records1.set_value(index, 'lastProgram', str(item["lastProgram"]))
            records1.set_value(index, 'acquisitionChannel', str(item["acquisitionChannel"]))
            records1.set_value(index, 'Eval_EULA', str(item["Eval_EULA"]))
            records1.set_value(index, 'recycled_date', str(item["recycled_date"]))
            records1.set_value(index, 'pushtoNetSuite', str(item["pushtoNetSuite"]))
            records1.set_value(index, 'Country__c', str(item["Country__c"]))
            records1.set_value(index, 'Lead_Lifecyle__c', str(item["Lead_Lifecyle__c"]))
            records1.set_value(index, 'MQL_Program_X__c', str(item["MQL_Program_X__c"]))
            records1.set_value(index, 'Sales_Activities_MQL__c', str(item["Sales_Activities_MQL__c"]))
            records1.set_value(index, 'Sourced_Industry__c', str(item["Sourced_Industry__c"]))
            records1.set_value(index, 'Sourced_Phone__c', str(item["Sourced_Phone__c"]))
            records1.set_value(index, 'State__c', str(item["State__c"]))
            records1.set_value(index, 'Subsidiary_Auto__c', str(item["Subsidiary_Auto__c"]))
            records1.set_value(index, 'Territory__c', str(item["Territory__c"]))
            records1.set_value(index, 'RecordTypeId', str(item["RecordTypeId"]))
            records1.set_value(index, 'Oppstageflag__c', str(item["Oppstageflag__c"]))
            records1.set_value(index, 'Contact_Status__c', str(item["Contact_Status__c"]))
            records1.set_value(index, 'Converted_Department__c', str(item["Converted_Department__c"]))
            records1.set_value(index, 'MQL_Offer_Name', str(item["MQL_Offer_Name"]))
            #records1.set_value(index, 'Channel_Offer', str(item["Channel_Offer"]))
            records1.set_value(index, 'Marketo_Lead_ID', str(item["Marketo_Lead_ID"]))
            records1.set_value(index, 'mktomerge', str(item["mktomerge"]))
            records1.set_value(index, 'External_Id__c', str(item["External_Id__c"]))
            records1.set_value(index, 'Subsidiary__c_contact', str(item["Subsidiary__c_contact"]))
            records1.set_value(index, 'Salesforce_Internal_Id__c', str(item["Salesforce_Internal_Id__c"]))
            records1.set_value(index, 'Date_of_First_Sale__c', str(item["Date_of_First_Sale__c"]))
            records1.set_value(index, 'Push_To_NetSuite_Reason__c', str(item["Push_To_NetSuite_Reason__c"]))
            records1.set_value(index, 'Contact_Us_Reason__c', str(item["Contact_Us_Reason__c"]))
            records1.set_value(index, 'VAT_ID__c', str(item["VAT_ID__c"]))
            records1.set_value(index, 'NS_Account_Owner__c', str(item["NS_Account_Owner__c"]))
            records1.set_value(index, 'Parent_Acct__c', str(item["Parent_Acct__c"]))
            records1.set_value(index, 'SF_Customer_Number__c', str(item["SF_Customer_Number__c"]))
            records1.set_value(index, 'Customer_Health__c', str(item["Customer_Health__c"]))
            records1.set_value(index, 'Customer_Tier__c', str(item["Customer_Tier__c"]))
            records1.set_value(index, 'Territory_Focus__c', str(item["Territory_Focus__c"]))
            records1.set_value(index, 'Country_Group__c', str(item["Country_Group__c"]))
            records1.set_value(index, 'Account_Currency_Formula__c', str(item["Account_Currency_Formula__c"]))
            records1.set_value(index, 'User_Subsidiary__c', str(item["User_Subsidiary__c"]))
            records1.set_value(index, 'CSM_Customer_Description__c', str(item["CSM_Customer_Description__c"]))
            records1.set_value(index, 'Health_Reason__c', str(item["Health_Reason__c"]))
            records1.set_value(index, 'Salesforce_Internal_Id_del__c', str(item["Salesforce_Internal_Id_del__c"]))
            records1.set_value(index, 'RecordTypeId_lead', str(item["RecordTypeId_lead"]))
            records1.set_value(index, 'Job_Function__c', str(item["Job_Function__c"]))
            records1.set_value(index, 'Domain_group__c', str(item["Domain_group__c"]))
            records1.set_value(index, 'Country__c_account', str(item["Country__c_account"]))
            records1.set_value(index, 'Owner_NetSuite_Id__c', str(item["Owner_NetSuite_Id__c"]))
            records1.set_value(index, 'Outdated_Region__c', str(item["Outdated_Region__c"]))
            records1.set_value(index, 'Hours_Since_MQL__c', str(item["Hours_Since_MQL__c"]))
            records1.set_value(index, 'companySFDC', str(item["companySFDC"]))
            records1.set_value(index, 'lastNameSFDC', str(item["lastNameSFDC"]))
            records1.set_value(index, 'Opportunity__c', str(item["Opportunity__c"]))
            records1.set_value(index, 'cSMFullName', str(item["cSMFullName"]))
            records1.set_value(index, 'Lead_Qualification_Date__c', str(item["Lead_Qualification_Date__c"]))
            records1.set_value(index, 'download_status', str(item["download_status"]))
            records1.set_value(index, 'Company_HQ_Location_State_Province__c',
                               str(item["Company_HQ_Location_State_Province__c"]))
            records1.set_value(index, 'Channel__c', str(item["Channel__c"]))
            records1.set_value(index, 'Channel_Partner__c', str(item["Channel_Partner__c"]))
            records1.set_value(index, 'Account_Description__c', str(item["Account_Description__c"]))
            records1.set_value(index, 'Account_Tier__c', str(item["Account_Tier__c"]))
            records1.set_value(index, 'Health_Score__c', str(item["Health_Score__c"]))
            records1.set_value(index, 'Health_Required_Actions__c', str(item["Health_Required_Actions__c"]))
            records1.set_value(index, 'Health_Action_Ownership__c', str(item["Health_Action_Ownership__c"]))
            records1.set_value(index, 'Health_Action_Status__c', str(item["Health_Action_Status__c"]))
            records1.set_value(index, 'Renewal_Risk__c', str(item["Renewal_Risk__c"]))
            records1.set_value(index, 'Renewal_Risk_Comment__c', str(item["Renewal_Risk_Comment__c"]))
            records1.set_value(index, 'Upsell_Risk__c', str(item["Upsell_Risk__c"]))
            records1.set_value(index, 'Upsell_Risk_Comment__c', str(item["Upsell_Risk_Comment__c"]))
            records1.set_value(index, 'Customer_Sat_Risk__c', str(item["Customer_Sat_Risk__c"]))
            records1.set_value(index, 'Customer_Sat_Risk_Comment__c', str(item["Customer_Sat_Risk_Comment__c"]))
            records1.set_value(index, 'Competitive_Threat_Risk__c', str(item["Competitive_Threat_Risk__c"]))
            records1.set_value(index, 'Competitive_Threat_Risk_Comment__c',
                               str(item["Competitive_Threat_Risk_Comment__c"]))
            records1.set_value(index, 'Strategic_Relationship_Risk__c', str(item["Strategic_Relationship_Risk__c"]))
            records1.set_value(index, 'Strategic_Relationship_Risk_Comment__c',
                               str(item["Strategic_Relationship_Risk_Comment__c"]))
            records1.set_value(index, 'Adoption_Risk__c', str(item["Adoption_Risk__c"]))
            records1.set_value(index, 'Adoption_Risk_Comment__c', str(item["Adoption_Risk_Comment__c"]))
            records1.set_value(index, 'Proven_Value_Risk__c', str(item["Proven_Value_Risk__c"]))
            records1.set_value(index, 'Proven_Value_Risk_Comment__c', str(item["Proven_Value_Risk_Comment__c"]))
            records1.set_value(index, 'Other_Risk__c', str(item["Other_Risk__c"]))
            records1.set_value(index, 'Other_Risk_Comment__c', str(item["Other_Risk_Comment__c"]))
            records1.set_value(index, 'Deployment_Progress__c', str(item["Deployment_Progress__c"]))
            records1.set_value(index, 'Laster_QBR__c', str(item["Laster_QBR__c"]))
            records1.set_value(index, 'Next_QBR__c', str(item["Next_QBR__c"]))
            records1.set_value(index, 'Assigned_CSM__c', str(item["Assigned_CSM__c"]))
            records1.set_value(index, 'LID__LinkedIn_Company_Id__c', str(item["LID__LinkedIn_Company_Id__c"]))
            records1.set_value(index, 'LID__LinkedIn_Member_Token__c', str(item["LID__LinkedIn_Member_Token__c"]))
            records1.set_value(index, 'LID__LinkedIn_Company_Id__c_account',
                               str(item["LID__LinkedIn_Company_Id__c_account"]))
            records1.set_value(index, 'qbdialer__Dials__c', str(item["qbdialer__Dials__c"]))
            records1.set_value(index, 'qbdialer__LastCallTime__c', str(item["qbdialer__LastCallTime__c"]))
            records1.set_value(index, 'qbdialer__ResponseTime__c', str(item["qbdialer__ResponseTime__c"]))
            records1.set_value(index, 'qbdialer__Dials__c_account', str(item["qbdialer__Dials__c_account"]))
            records1.set_value(index, 'qbdialer__LastCallTime__c_account',
                               str(item["qbdialer__LastCallTime__c_account"]))
            records1.set_value(index, 'qbdialer__ResponseTime__c_account',
                               str(item["qbdialer__ResponseTime__c_account"]))
            records1.set_value(index, 'UniqueEntry__Contact_Dupes_Ignored__c',
                               str(item["UniqueEntry__Contact_Dupes_Ignored__c"]))
            records1.set_value(index, 'UniqueEntry__Lead_Dupes_Ignored__c',
                               str(item["UniqueEntry__Lead_Dupes_Ignored__c"]))
            records1.set_value(index, 'UniqueEntry__Account_Dupes_Ignored__c',
                               str(item["UniqueEntry__Account_Dupes_Ignored__c"]))
            records1.set_value(index, 'preMQLProgramAttribution', str(item["preMQLProgramAttribution"]))
            records1.set_value(index, 'mQLProgramAttribution', str(item["mQLProgramAttribution"]))
            records1.set_value(index, 'sQLProgramAttribution', str(item["sQLProgramAttribution"]))
            records1.set_value(index, 'sALProgramAttribution', str(item["sALProgramAttribution"]))
            records1.set_value(index, 'winProgramAttribution', str(item["winProgramAttribution"]))
            records1.set_value(index, 'Days_Since_MQLs__c', str(item["Days_Since_MQLs__c"]))
            records1.set_value(index, 'Days_Since_MQLs_del__c', str(item["Days_Since_MQLs_del__c"]))
            records1.set_value(index, 'interestTIC', str(item["interestTIC"]))
            records1.set_value(index, 'TIC_Credentials_Issue_Date__c', str(item["TIC_Credentials_Issue_Date__c"]))
            records1.set_value(index, 'NanoCloud_Account_Created_Date__c',
                               str(item["NanoCloud_Account_Created_Date__c"]))
            records1.set_value(index, 'of_calls_per_lead__c', str(item["of_calls_per_lead__c"]))
            records1.set_value(index, 'companySFDCClone', str(item["companySFDCClone"]))
            records1.set_value(index, 'lastNameSFDCClone', str(item["lastNameSFDCClone"]))
            records1.set_value(index, 'acquisition_Channel_temp', str(item["acquisition_Channel_temp"]))
            records1.set_value(index, 'updatedFromAPI', str(item["updatedFromAPI"]))
            records1.set_value(index, 'RingLead_Status', str(item["RingLead_Status"]))
            records1.set_value(index, 'mKTOdummyfield', str(item["mKTOdummyfield"]))
            records1.set_value(index, 'MQL_Program_temp', str(item["MQL_Program_temp"]))
            records1.set_value(index, 'revenueCycleDatesKnown', str(item["revenueCycleDatesKnown"]))
            records1.set_value(index, 'revenueCycleDatesEngaged', str(item["revenueCycleDatesEngaged"]))
            records1.set_value(index, 'revenueCycleDatesMQL', str(item["revenueCycleDatesMQL"]))
            records1.set_value(index, 'revenueCycleDatesASDRAccepted', str(item["revenueCycleDatesASDRAccepted"]))
            records1.set_value(index, 'revenueCycleDatesSQL', str(item["revenueCycleDatesSQL"]))
            records1.set_value(index, 'revenueCycleDatesPipeline', str(item["revenueCycleDatesPipeline"]))
            records1.set_value(index, 'revenueCycleDatesBestCase', str(item["revenueCycleDatesBestCase"]))
            records1.set_value(index, 'revenueCycleDatesCommit', str(item["revenueCycleDatesCommit"]))
            records1.set_value(index, 'revenueCycleDatesCustomer', str(item["revenueCycleDatesCustomer"]))
            records1.set_value(index, 'revenueCycleDatesRenewal', str(item["revenueCycleDatesRenewal"]))
            records1.set_value(index, 'revenueCycleDatesUpsell', str(item["revenueCycleDatesUpsell"]))
            records1.set_value(index, 'revenueCycleDatesExpired', str(item["revenueCycleDatesExpired"]))
            records1.set_value(index, 'revenueCycleDatesInactive', str(item["revenueCycleDatesInactive"]))
            records1.set_value(index, 'revenueCycleDatesBadData', str(item["revenueCycleDatesBadData"]))
            records1.set_value(index, 'revenueCycleDatesUnqualified', str(item["revenueCycleDatesUnqualified"]))
            records1.set_value(index, 'revenueCycleDatesRecycled', str(item["revenueCycleDatesRecycled"]))
            records1.set_value(index, 'revenueCycleDatesReturntoADR', str(item["revenueCycleDatesReturntoADR"]))
            records1.set_value(index, 'revenueCycleDatesLost', str(item["revenueCycleDatesLost"]))
            records1.set_value(index, 'revenueCycleCurrentStage', str(item["revenueCycleCurrentStage"]))
            records1.set_value(index, 'SD_Lead_Notes__c', str(item["SD_Lead_Notes__c"]))
            records1.set_value(index, 'SD_Company_Address__c', str(item["SD_Company_Address__c"]))
            records1.set_value(index, 'SD_Company_City__c', str(item["SD_Company_City__c"]))
            records1.set_value(index, 'SD_Business_Description__c', str(item["SD_Business_Description__c"]))
            records1.set_value(index, 'SD_Company_Country__c', str(item["SD_Company_Country__c"]))
            records1.set_value(index, 'SD_IT_Budget__c', str(item["SD_IT_Budget__c"]))
            records1.set_value(index, 'SD_IT_Employees__c', str(item["SD_IT_Employees__c"]))
            records1.set_value(index, 'SD_Company_Postal_Code__c', str(item["SD_Company_Postal_Code__c"]))
            records1.set_value(index, 'SD_Tech_Business_Intelligence__c',
                               str(item["SD_Tech_Business_Intelligence__c"]))
            records1.set_value(index, 'SD_Tech_CRM_MarketingAutomation__c',
                               str(item["SD_Tech_CRM_MarketingAutomation__c"]))
            records1.set_value(index, 'SD_Tech_DataManagement__c', str(item["SD_Tech_DataManagement__c"]))
            records1.set_value(index, 'SD_Tech_Data_Storage__c', str(item["SD_Tech_Data_Storage__c"]))
            records1.set_value(index, 'SD_Tech_Databases__c', str(item["SD_Tech_Databases__c"]))
            records1.set_value(index, 'SD_Tech_ERP_HR_HCM_FI__c', str(item["SD_Tech_ERP_HR_HCM_FI__c"]))
            records1.set_value(index, 'SD_Tech_Enterprise_Applications__c',
                               str(item["SD_Tech_Enterprise_Applications__c"]))
            records1.set_value(index, 'SD_Tech_Hardware_OS_SystemsEnvironment__c',
                               str(item["SD_Tech_Hardware_OS_SystemsEnvironment__c"]))
            records1.set_value(index, 'SD_Tech_ITSM__c', str(item["SD_Tech_ITSM__c"]))
            records1.set_value(index, 'SD_Tech_Languages__c', str(item["SD_Tech_Languages__c"]))
            records1.set_value(index, 'SD_Tech_Programming_Tools__c', str(item["SD_Tech_Programming_Tools__c"]))
            records1.set_value(index, 'SD_Company_Address__c_contact', str(item["SD_Company_Address__c_contact"]))
            records1.set_value(index, 'SD_Company_City__c_contact', str(item["SD_Company_City__c_contact"]))
            records1.set_value(index, 'SD_Company_Postal_Code__c_contact',
                               str(item["SD_Company_Postal_Code__c_contact"]))
            records1.set_value(index, 'Phone_1st_3_Digits__c', str(item["Phone_1st_3_Digits__c"]))
            records1.set_value(index, 'Sales_Activities_MQL_Dials__c', str(item["Sales_Activities_MQL_Dials__c"]))
            records1.set_value(index, 'i__CreatedForUser__c', str(item["i__CreatedForUser__c"]))
            records1.set_value(index, 'i__DaysSinceLastMail__c', str(item["i__DaysSinceLastMail__c"]))
            records1.set_value(index, 'i__LastInboundMail__c', str(item["i__LastInboundMail__c"]))
            records1.set_value(index, 'i__LastInboundSent__c', str(item["i__LastInboundSent__c"]))
            records1.set_value(index, 'i__LastInboundTime__c', str(item["i__LastInboundTime__c"]))
            records1.set_value(index, 'i__LastMailSent__c', str(item["i__LastMailSent__c"]))
            records1.set_value(index, 'i__LastMailTimeDelta__c', str(item["i__LastMailTimeDelta__c"]))
            records1.set_value(index, 'i__LastMailTime__c', str(item["i__LastMailTime__c"]))
            records1.set_value(index, 'i__LastMail__c', str(item["i__LastMail__c"]))
            records1.set_value(index, 'i__LastOutboundMail__c', str(item["i__LastOutboundMail__c"]))
            records1.set_value(index, 'i__LastOutboundSent__c', str(item["i__LastOutboundSent__c"]))
            records1.set_value(index, 'i__LastOutboundTime__c', str(item["i__LastOutboundTime__c"]))
            records1.set_value(index, 'i__OtherEmails__c', str(item["i__OtherEmails__c"]))
            records1.set_value(index, 'i__DaysSinceLastMail__c_account',
                               str(item["i__DaysSinceLastMail__c_account"]))
            records1.set_value(index, 'i__LastInboundMail__c_account', str(item["i__LastInboundMail__c_account"]))
            records1.set_value(index, 'i__LastInboundSent__c_account', str(item["i__LastInboundSent__c_account"]))
            records1.set_value(index, 'i__LastInboundTime__c_account', str(item["i__LastInboundTime__c_account"]))
            records1.set_value(index, 'i__LastMailSent__c_account', str(item["i__LastMailSent__c_account"]))
            records1.set_value(index, 'i__LastMailTimeDelta__c_account',
                               str(item["i__LastMailTimeDelta__c_account"]))
            records1.set_value(index, 'i__LastMailTime__c_account', str(item["i__LastMailTime__c_account"]))
            records1.set_value(index, 'i__LastMail__c_account', str(item["i__LastMail__c_account"]))
            records1.set_value(index, 'i__LastOutboundMail__c_account', str(item["i__LastOutboundMail__c_account"]))
            records1.set_value(index, 'i__LastOutboundSent__c_account', str(item["i__LastOutboundSent__c_account"]))
            records1.set_value(index, 'i__LastOutboundTime__c_account', str(item["i__LastOutboundTime__c_account"]))
            records1.set_value(index, 'mktotempfield', str(item["mktotempfield"]))
            records1.set_value(index, 'sDITBudgetC', str(item["sDITBudgetC"]))
            records1.set_value(index, 'sDITEmployeesC', str(item["sDITEmployeesC"]))
            records1.set_value(index, 'sDTechBusinessIntelligenceC', str(item["sDTechBusinessIntelligenceC"]))
            records1.set_value(index, 'sDTechCRMMarketingAutomationC', str(item["sDTechCRMMarketingAutomationC"]))
            records1.set_value(index, 'sDTechDataManagementC', str(item["sDTechDataManagementC"]))
            records1.set_value(index, 'sDTechDataStorageC', str(item["sDTechDataStorageC"]))
            records1.set_value(index, 'sDTechDatabasesC', str(item["sDTechDatabasesC"]))
            records1.set_value(index, 'sDTechERPHRHCMFIC', str(item["sDTechERPHRHCMFIC"]))
            records1.set_value(index, 'sDTechEnterpriseApplicationsC', str(item["sDTechEnterpriseApplicationsC"]))
            records1.set_value(index, 'sDTechHardwareOSSystemsEnvironmentC',
                               str(item["sDTechHardwareOSSystemsEnvironmentC"]))
            records1.set_value(index, 'sDTechITSMC', str(item["sDTechITSMC"]))
            records1.set_value(index, 'sDTechLanguagesC', str(item["sDTechLanguagesC"]))
            records1.set_value(index, 'sDTechProgrammingToolsC', str(item["sDTechProgrammingToolsC"]))
            records1.set_value(index, 'sDBusinessDescriptionC', str(item["sDBusinessDescriptionC"]))
            records1.set_value(index, 'sDCompanyCountryC', str(item["sDCompanyCountryC"]))
            records1.set_value(index, 'mostRecentLeadSource', str(item["mostRecentLeadSource"]))
            records1.set_value(index, 'mostRecentLeadSourceDetail', str(item["mostRecentLeadSourceDetail"]))
            records1.set_value(index, 'Product_Solution_Integration_Cloud__c',
                               str(item["Product_Solution_Integration_Cloud__c"]))
            records1.set_value(index, 'updateFromDiscoverOrg', str(item["updateFromDiscoverOrg"]))
            records1.set_value(index, 'qbdialer__CloseDate__c', str(item["qbdialer__CloseDate__c"]))
            records1.set_value(index, 'qbdialer__CloseScore__c', str(item["qbdialer__CloseScore__c"]))
            records1.set_value(index, 'qbdialer__ContactDate__c', str(item["qbdialer__ContactDate__c"]))
            records1.set_value(index, 'qbdialer__ContactScoreId__c', str(item["qbdialer__ContactScoreId__c"]))
            records1.set_value(index, 'qbdialer__ContactScore__c', str(item["qbdialer__ContactScore__c"]))
            records1.set_value(index, 'qbdialer__TimeZoneSidKey__c', str(item["qbdialer__TimeZoneSidKey__c"]))
            records1.set_value(index, 'qbdialer__TimeZoneSidKey__c_account',
                               str(item["qbdialer__TimeZoneSidKey__c_account"]))
            records1.set_value(index, 'NPS_Contact__c', str(item["NPS_Contact__c"]))
            records1.set_value(index, 'Executive_Sponsor__c', str(item["Executive_Sponsor__c"]))
            records1.set_value(index, 'Gainsight_Health__c', str(item["Gainsight_Health__c"]))
            records1.set_value(index, 'Renewal_Status__c', str(item["Renewal_Status__c"]))
            records1.set_value(index, 'Renewal_Type__c', str(item["Renewal_Type__c"]))
            records1.set_value(index, 'externalCompanyId', str(item["externalCompanyId"]))
            records1.set_value(index, 'sf_leadid__c', str(item["sf_leadid__c"]))
            records1.set_value(index, 'sf_contactid__c', str(item["sf_contactid__c"]))
            records1.set_value(index, 'Mass_Update_for_Marketo__c', str(item["Mass_Update_for_Marketo__c"]))
            records1.set_value(index, 'DSCORGPKG__DiscoverOrg_Created_On__c',
                               str(item["DSCORGPKG__DiscoverOrg_Created_On__c"]))
            records1.set_value(index, 'DSCORGPKG__External_DiscoverOrg_Id__c',
                               str(item["DSCORGPKG__External_DiscoverOrg_Id__c"]))
            records1.set_value(index, 'DSCORGPKG__department__c', str(item["DSCORGPKG__department__c"]))
            records1.set_value(index, 'DSCORGPKG__DiscoverOrg_Created_On__c_account',
                               str(item["DSCORGPKG__DiscoverOrg_Created_On__c_account"]))
            records1.set_value(index, 'DSCORGPKG__External_DiscoverOrg_Id__c_account',
                               str(item["DSCORGPKG__External_DiscoverOrg_Id__c_account"]))
            records1.set_value(index, 'Renew_Loss__c', str(item["Renew_Loss__c"]))
            records1.set_value(index, 'Customer_Categorization__c', str(item["Customer_Categorization__c"]))
            records1.set_value(index, 'reasonsNotPromoted', str(item["reasonsNotPromoted"]))
            records1.set_value(index, 'CAB_Member__c', str(item["CAB_Member__c"]))
            records1.set_value(index, 'White_Glove__c', str(item["White_Glove__c"]))
            records1.set_value(index, 'X1_How_is_the_customer_measuring_success__c',
                               str(item["X1_How_is_the_customer_measuring_success__c"]))
            records1.set_value(index, 'X2_Are_they_we_achieving_that_success__c',
                               str(item["X2_Are_they_we_achieving_that_success__c"]))
            records1.set_value(index, 'X3_How_has_their_experience_been__c',
                               str(item["X3_How_has_their_experience_been__c"]))
            records1.set_value(index, 'externalSalesPersonId', str(item["externalSalesPersonId"]))
            records1.set_value(index, 'End_User_ACV__c', str(item["End_User_ACV__c"]))
            records1.set_value(index, 'End_User_TCV__c', str(item["End_User_TCV__c"]))
            records1.set_value(index, 'Partner_ACV__c', str(item["Partner_ACV__c"]))
            records1.set_value(index, 'Partner_TCV__c', str(item["Partner_TCV__c"]))
            records1.set_value(index, 'Reseller_ACV__c', str(item["Reseller_ACV__c"]))
            records1.set_value(index, 'Reseller_TCV__c', str(item["Reseller_TCV__c"]))
            records1.set_value(index, 'aWSUsage', str(item["aWSUsage"]))
            records1.set_value(index, 'aWSInfoShare', str(item["aWSInfoShare"]))
            records1.set_value(index, 'qbdialer__CloseDate__c_account', str(item["qbdialer__CloseDate__c_account"]))
            records1.set_value(index, 'qbdialer__CloseScore__c_account',
                               str(item["qbdialer__CloseScore__c_account"]))
            records1.set_value(index, 'CSM_Email_Address__c', str(item["CSM_Email_Address__c"]))
            records1.set_value(index, 'CSM_Phone_Number__c', str(item["CSM_Phone_Number__c"]))
            records1.set_value(index, 'Account_Channel_Tier__c', str(item["Account_Channel_Tier__c"]))
            records1.set_value(index, 'landing_page_language', str(item["landing_page_language"]))
            records1.set_value(index, 'Assigned_CSA__c', str(item["Assigned_CSA__c"]))
            records1.set_value(index, 'Buyer_Journey_Stage__c', str(item["Buyer_Journey_Stage__c"]))
            records1.set_value(index, 'AVA__AVAAI_date_added__c', str(item["AVA__AVAAI_date_added__c"]))
            records1.set_value(index, 'AVA__AVAAI_first_message_date__c',
                               str(item["AVA__AVAAI_first_message_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_hot_lead__c', str(item["AVA__AVAAI_hot_lead__c"]))
            records1.set_value(index, 'AVA__AVAAI_hot_lead_date__c', str(item["AVA__AVAAI_hot_lead_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_last_message_date__c',
                               str(item["AVA__AVAAI_last_message_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_last_response_date__c',
                               str(item["AVA__AVAAI_last_response_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_lead_at_risk__c', str(item["AVA__AVAAI_lead_at_risk__c"]))
            records1.set_value(index, 'AVA__AVAAI_lead_at_risk_date__c',
                               str(item["AVA__AVAAI_lead_at_risk_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_options__c', str(item["AVA__AVAAI_options__c"]))
            records1.set_value(index, 'AVA__AVAAI_score__c', str(item["AVA__AVAAI_score__c"]))
            records1.set_value(index, 'AVA__AVAAI_status__c', str(item["AVA__AVAAI_status__c"]))
            records1.set_value(index, 'AVA__Campaign__c', str(item["AVA__Campaign__c"]))
            records1.set_value(index, 'IsPartner', str(item["IsPartner"]))
            records1.set_value(index, 'IsCustomerPortal', str(item["IsCustomerPortal"]))
            records1.set_value(index, 'Account_OTRS_ID__c', str(item["Account_OTRS_ID__c"]))
            records1.set_value(index, 'Total_Active_User_Support_Licenses__c',
                               str(item["Total_Active_User_Support_Licenses__c"]))
            records1.set_value(index, 'Total_Portal_Support_Users__c', str(item["Total_Portal_Support_Users__c"]))
            records1.set_value(index, 'Customer_Preferred_Region__c', str(item["Customer_Preferred_Region__c"]))
            records1.set_value(index, 'Active_Support_User__c', str(item["Active_Support_User__c"]))
            records1.set_value(index, 'License_Company_Name__c', str(item["License_Company_Name__c"]))
            records1.set_value(index, 'License_End_Date__c', str(item["License_End_Date__c"]))
            records1.set_value(index, 'License_Start_Date__c', str(item["License_Start_Date__c"]))
            records1.set_value(index, 'Primary_Support_Contact__c', str(item["Primary_Support_Contact__c"]))
            records1.set_value(index, 'Tier__c', str(item["Tier__c"]))
            records1.set_value(index, 'Support_Contact__c', str(item["Support_Contact__c"]))
            records1.set_value(index, 'customer_id__c', str(item["customer_id__c"]))
            records1.set_value(index, 'License_Service_Level__c', str(item["License_Service_Level__c"]))
            records1.set_value(index, 'account_code', str(item["account_code"]))
            records1.set_value(index, 'Executive_Contact__c', str(item["Executive_Contact__c"]))
            records1.set_value(index, 'Champion_Contact__c', str(item["Champion_Contact__c"]))
            records1.set_value(index, 'Billing_Contact__c', str(item["Billing_Contact__c"]))
            records1.set_value(index, 'Reference_Contact__c', str(item["Reference_Contact__c"]))
            records1.set_value(index, 'Architect_Contact__c', str(item["Architect_Contact__c"]))
            records1.set_value(index, 'Total_Opportunities__c', str(item["Total_Opportunities__c"]))
            records1.set_value(index, 'Total_Open_Opportunities__c', str(item["Total_Open_Opportunities__c"]))
            records1.set_value(index, 'Super_Contact_User__c', str(item["Super_Contact_User__c"]))
            records1.set_value(index, 'Conversica_Outreach_Context__c', str(item["Conversica_Outreach_Context__c"]))
            records1.set_value(index, 'Conversica_Inquiry_Verb__c', str(item["Conversica_Inquiry_Verb__c"]))
            records1.set_value(index, 'Conversica_Outreach_Title__c', str(item["Conversica_Outreach_Title__c"]))
            records1.set_value(index, 'CSM_Brief_Company_Overview__c', str(item["CSM_Brief_Company_Overview__c"]))
            records1.set_value(index, 'CSM_Brief_Background_on_Account__c',
                               str(item["CSM_Brief_Background_on_Account__c"]))
            records1.set_value(index, 'CSM_Business_Case_Why_Talend__c',
                               str(item["CSM_Business_Case_Why_Talend__c"]))
            records1.set_value(index, 'CSM_Competitive_Landscape__c', str(item["CSM_Competitive_Landscape__c"]))
            records1.set_value(index, 'A_Initial_Adoption_Usage__c', str(item["A_Initial_Adoption_Usage__c"]))
            records1.set_value(index, 'A_Initial_Business_Case__c', str(item["A_Initial_Business_Case__c"]))
            records1.set_value(index, 'A_Initial_Success_Criteria__c', str(item["A_Initial_Success_Criteria__c"]))
            records1.set_value(index, 'A_Initial_Use_Case__c', str(item["A_Initial_Use_Case__c"]))
            records1.set_value(index, 'D_Initial_Adoption_Usage__c', str(item["D_Initial_Adoption_Usage__c"]))
            records1.set_value(index, 'D_Initial_Business_Case__c', str(item["D_Initial_Business_Case__c"]))
            records1.set_value(index, 'D_Initial_Success_Criteria__c', str(item["D_Initial_Success_Criteria__c"]))
            records1.set_value(index, 'D_Initial_Use_Case__c', str(item["D_Initial_Use_Case__c"]))
            records1.set_value(index, 'E_Initial_Deployment__c', str(item["E_Initial_Deployment__c"]))
            records1.set_value(index, 'M_Initial_Business_Case_Location__c',
                               str(item["M_Initial_Business_Case_Location__c"]))
            records1.set_value(index, 'M_Initial_Success_Criteria_Location__c',
                               str(item["M_Initial_Success_Criteria_Location__c"]))
            records1.set_value(index, 'M_Initial_Use_Case_Location__c', str(item["M_Initial_Use_Case_Location__c"]))
            records1.set_value(index, 'MAE_Presentation_URL__c', str(item["MAE_Presentation_URL__c"]))
            records1.set_value(index, 'MAE_Record_Session_URL__c', str(item["MAE_Record_Session_URL__c"]))
            records1.set_value(index, 'Web_User_Login__c', str(item["Web_User_Login__c"]))
            records1.set_value(index, 'LeadsProfiler__Business_Group__c',
                               str(item["LeadsProfiler__Business_Group__c"]))
            records1.set_value(index, 'LeadsProfiler__Business_Group_ref__c',
                               str(item["LeadsProfiler__Business_Group_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Buyer_Persona__c',
                               str(item["LeadsProfiler__Buyer_Persona__c"]))
            records1.set_value(index, 'LeadsProfiler__Buyer_Persona_ref__c',
                               str(item["LeadsProfiler__Buyer_Persona_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__ChangeRankReason__c',
                               str(item["LeadsProfiler__ChangeRankReason__c"]))
            records1.set_value(index, 'LeadsProfiler__City__c', str(item["LeadsProfiler__City__c"]))
            records1.set_value(index, 'LeadsProfiler__City_ref__c', str(item["LeadsProfiler__City_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Company_Profile__c',
                               str(item["LeadsProfiler__Company_Profile__c"]))
            records1.set_value(index, 'LeadsProfiler__Company_Profile_ref__c',
                               str(item["LeadsProfiler__Company_Profile_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Company_Revenue__c',
                               str(item["LeadsProfiler__Company_Revenue__c"]))
            records1.set_value(index, 'LeadsProfiler__Company_Revenue_ref__c',
                               str(item["LeadsProfiler__Company_Revenue_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Company_Size__c', str(item["LeadsProfiler__Company_Size__c"]))
            records1.set_value(index, 'LeadsProfiler__Company_Size_ref__c',
                               str(item["LeadsProfiler__Company_Size_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Country__c', str(item["LeadsProfiler__Country__c"]))
            records1.set_value(index, 'LeadsProfiler__Country_ref__c', str(item["LeadsProfiler__Country_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__DataObject__c', str(item["LeadsProfiler__DataObject__c"]))
            records1.set_value(index, 'LeadsProfiler__OriginalRank__c', str(item["LeadsProfiler__OriginalRank__c"]))
            records1.set_value(index, 'LeadsProfiler__OriginalRank_ref__c',
                               str(item["LeadsProfiler__OriginalRank_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Probability_Delta__c',
                               str(item["LeadsProfiler__Probability_Delta__c"]))
            records1.set_value(index, 'LeadsProfiler__Probability_Delta_ref__c',
                               str(item["LeadsProfiler__Probability_Delta_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_Last_Update__c',
                               str(item["LeadsProfiler__SalesPredict_Last_Update__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_Last_Update_ref__c',
                               str(item["LeadsProfiler__SalesPredict_Last_Update_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_Rank__c',
                               str(item["LeadsProfiler__SalesPredict_Rank__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_report_rank__c',
                               str(item["LeadsProfiler__SalesPredict_report_rank__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_report_rank_ref__c',
                               str(item["LeadsProfiler__SalesPredict_report_rank_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Score__c', str(item["LeadsProfiler__Score__c"]))
            records1.set_value(index, 'LeadsProfiler__Score_ref__c', str(item["LeadsProfiler__Score_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Solution_Fit__c', str(item["LeadsProfiler__Solution_Fit__c"]))
            records1.set_value(index, 'LeadsProfiler__Solution_Fit_ref__c',
                               str(item["LeadsProfiler__Solution_Fit_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__State__c', str(item["LeadsProfiler__State__c"]))
            records1.set_value(index, 'LeadsProfiler__State_ref__c', str(item["LeadsProfiler__State_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Street__c', str(item["LeadsProfiler__Street__c"]))
            records1.set_value(index, 'LeadsProfiler__Street_ref__c', str(item["LeadsProfiler__Street_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Title__c', str(item["LeadsProfiler__Title__c"]))
            records1.set_value(index, 'LeadsProfiler__Title_ref__c', str(item["LeadsProfiler__Title_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Vertical__c', str(item["LeadsProfiler__Vertical__c"]))
            records1.set_value(index, 'LeadsProfiler__Vertical_ref__c', str(item["LeadsProfiler__Vertical_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Business_Group__c_account',
                               str(item["LeadsProfiler__Business_Group__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Business_Group_ref__c_account',
                               str(item["LeadsProfiler__Business_Group_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Buyer_Persona__c_account',
                               str(item["LeadsProfiler__Buyer_Persona__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Buyer_Persona_ref__c_account',
                               str(item["LeadsProfiler__Buyer_Persona_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__ChangeRankReason__c_account',
                               str(item["LeadsProfiler__ChangeRankReason__c_account"]))
            records1.set_value(index, 'LeadsProfiler__City__c_account', str(item["LeadsProfiler__City__c_account"]))
            records1.set_value(index, 'LeadsProfiler__City_ref__c_account',
                               str(item["LeadsProfiler__City_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Company_Profile__c_account',
                               str(item["LeadsProfiler__Company_Profile__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Company_Profile_ref__c_account',
                               str(item["LeadsProfiler__Company_Profile_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Company_Revenue__c_account',
                               str(item["LeadsProfiler__Company_Revenue__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Company_Revenue_ref__c_account',
                               str(item["LeadsProfiler__Company_Revenue_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Company_Size__c_account',
                               str(item["LeadsProfiler__Company_Size__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Company_Size_ref__c_account',
                               str(item["LeadsProfiler__Company_Size_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Country__c_account',
                               str(item["LeadsProfiler__Country__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Country_ref__c_account',
                               str(item["LeadsProfiler__Country_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__DataObject__c_account',
                               str(item["LeadsProfiler__DataObject__c_account"]))
            records1.set_value(index, 'LeadsProfiler__OriginalRank__c_account',
                               str(item["LeadsProfiler__OriginalRank__c_account"]))
            records1.set_value(index, 'LeadsProfiler__OriginalRank_ref__c_account',
                               str(item["LeadsProfiler__OriginalRank_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Probability_Delta__c_account',
                               str(item["LeadsProfiler__Probability_Delta__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Probability_Delta_ref__c_account',
                               str(item["LeadsProfiler__Probability_Delta_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Renewal_Probability_Delta__c',
                               str(item["LeadsProfiler__Renewal_Probability_Delta__c"]))
            records1.set_value(index, 'LeadsProfiler__Renewal_Probability_Delta_ref__c',
                               str(item["LeadsProfiler__Renewal_Probability_Delta_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__Renewal_Score__c',
                               str(item["LeadsProfiler__Renewal_Score__c"]))
            records1.set_value(index, 'LeadsProfiler__Renewal_Score_ref__c',
                               str(item["LeadsProfiler__Renewal_Score_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_Renewal_Rank__c',
                               str(item["LeadsProfiler__SalesPredict_Renewal_Rank__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_Renewal_report_rank__c',
                               str(item["LeadsProfiler__SalesPredict_Renewal_report_rank__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_Renewal_report_rank_ref__c',
                               str(item["LeadsProfiler__SalesPredict_Renewal_report_rank_ref__c"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_rank__c_account',
                               str(item["LeadsProfiler__SalesPredict_rank__c_account"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_report_rank__c_account',
                               str(item["LeadsProfiler__SalesPredict_report_rank__c_account"]))
            records1.set_value(index, 'LeadsProfiler__SalesPredict_report_rank_ref__c_account',
                               str(item["LeadsProfiler__SalesPredict_report_rank_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Score__c_account',
                               str(item["LeadsProfiler__Score__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Score_ref__c_account',
                               str(item["LeadsProfiler__Score_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Solution_Fit__c_account',
                               str(item["LeadsProfiler__Solution_Fit__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Solution_Fit_ref__c_account',
                               str(item["LeadsProfiler__Solution_Fit_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__State__c_account',
                               str(item["LeadsProfiler__State__c_account"]))
            records1.set_value(index, 'LeadsProfiler__State_ref__c_account',
                               str(item["LeadsProfiler__State_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Street__c_account',
                               str(item["LeadsProfiler__Street__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Street_ref__c_account',
                               str(item["LeadsProfiler__Street_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Title__c_account',
                               str(item["LeadsProfiler__Title__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Title_ref__c_account',
                               str(item["LeadsProfiler__Title_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Vertical__c_account',
                               str(item["LeadsProfiler__Vertical__c_account"]))
            records1.set_value(index, 'LeadsProfiler__Vertical_ref__c_account',
                               str(item["LeadsProfiler__Vertical_ref__c_account"]))
            records1.set_value(index, 'LeadsProfiler__OriginalRank__c_contact',
                               str(item["LeadsProfiler__OriginalRank__c_contact"]))
            records1.set_value(index, 'LeadsProfiler__Score__c_contact',
                               str(item["LeadsProfiler__Score__c_contact"]))
            records1.set_value(index, 'Best_Service_LevelOn__c', str(item["Best_Service_LevelOn__c"]))
            records1.set_value(index, 'Total_Gold_License__c', str(item["Total_Gold_License__c"]))
            records1.set_value(index, 'Total_Mission_Critical__c', str(item["Total_Mission_Critical__c"]))
            records1.set_value(index, 'Total_Platinum_License__c', str(item["Total_Platinum_License__c"]))
            records1.set_value(index, 'iKOCompanyName', str(item["iKOCompanyName"]))
            records1.set_value(index, 'iKOCompanyPhone', str(item["iKOCompanyPhone"]))
            records1.set_value(index, 'iKOCompanySize', str(item["iKOCompanySize"]))
            records1.set_value(index, 'iKOCompanyWebsite', str(item["iKOCompanyWebsite"]))
            records1.set_value(index, 'iKOCountry', str(item["iKOCountry"]))
            records1.set_value(index, 'iKOEmailMain', str(item["iKOEmailMain"]))
            records1.set_value(index, 'iKOFirstName', str(item["iKOFirstName"]))
            records1.set_value(index, 'iKOInsertTime', str(item["iKOInsertTime"]))
            records1.set_value(index, 'iKOJobCategory', str(item["iKOJobCategory"]))
            records1.set_value(index, 'iKOJobTitle', str(item["iKOJobTitle"]))
            records1.set_value(index, 'iKOLastName', str(item["iKOLastName"]))
            records1.set_value(index, 'iKOLeadIndustry', str(item["iKOLeadIndustry"]))
            records1.set_value(index, 'iKOLeadOwner', str(item["iKOLeadOwner"]))
            records1.set_value(index, 'iKOLeadPhone', str(item["iKOLeadPhone"]))
            records1.set_value(index, 'Interest_DP__c', str(item["Interest_DP__c"]))
            records1.set_value(index, 'campaign_creative', str(item["campaign_creative"]))
            records1.set_value(index, 'Opp_Created_After_Added_to_Conversica__c',
                               str(item["Opp_Created_After_Added_to_Conversica__c"]))
            records1.set_value(index, 'Is_Current_License_Expired__c', str(item["Is_Current_License_Expired__c"]))
            records1.set_value(index, 'successfactors_id__c', str(item["successfactors_id__c"]))
            records1.set_value(index, 'successfactors_id__c_contact', str(item["successfactors_id__c_contact"]))
            records1.set_value(index, 'Website_behavior_summary__c', str(item["Website_behavior_summary__c"]))
            records1.set_value(index, 'HW__c', str(item["HW__c"]))
            records1.set_value(index, 'MapR__c', str(item["MapR__c"]))
            records1.set_value(index, 'Teradata_EDW_Teradata_TDH_Teradata__c',
                               str(item["Teradata_EDW_Teradata_TDH_Teradata__c"]))
            records1.set_value(index, 'AWS_AWS_Redshift_AWS_EMR_AWS_spar__c',
                               str(item["AWS_AWS_Redshift_AWS_EMR_AWS_spar__c"]))
            records1.set_value(index, 'Google_Google_BigQuery_Google_DataP__c',
                               str(item["Google_Google_BigQuery_Google_DataP__c"]))
            records1.set_value(index, 'HP_Vertica__c', str(item["HP_Vertica__c"]))
            records1.set_value(index, 'MongoDB__c', str(item["MongoDB__c"]))
            records1.set_value(index, 'DataStax__c', str(item["DataStax__c"]))
            records1.set_value(index, 'Tableau__c', str(item["Tableau__c"]))
            records1.set_value(index, 'Couchbase__c', str(item["Couchbase__c"]))
            records1.set_value(index, 'Qlik__c', str(item["Qlik__c"]))
            records1.set_value(index, 'CDH__c', str(item["CDH__c"]))
            records1.set_value(index, 'NS_Transaction_Customer__c', str(item["NS_Transaction_Customer__c"]))
            records1.set_value(index, 'CSM_Team_Manager__c', str(item["CSM_Team_Manager__c"]))
            records1.set_value(index, 'Customer_One_Drive_Location__c', str(item["Customer_One_Drive_Location__c"]))
            records1.set_value(index, 'Do_not_allow_super_users__c', str(item["Do_not_allow_super_users__c"]))
            records1.set_value(index, 'Gainsight_C360__c', str(item["Gainsight_C360__c"]))
            #records1.set_value(index, 'tic_username', str(item["tic_username"]))
            records1.set_value(index, 'Date_of_1st_Renewal_Sale__c', str(item["Date_of_1st_Renewal_Sale__c"]))
            records1.set_value(index, 'Lead_Source_2__c', str(item["Lead_Source_2__c"]))
            records1.set_value(index, 'mktoLeadOwnerFirstName', str(item["mktoLeadOwnerFirstName"]))
            records1.set_value(index, 'mktoLeadOwnerLastName', str(item["mktoLeadOwnerLastName"]))
            records1.set_value(index, 'mktoLeadOwnerEmailAddress', str(item["mktoLeadOwnerEmailAddress"]))
            records1.set_value(index, 'mktoLeadOwnerPhoneNumber', str(item["mktoLeadOwnerPhoneNumber"]))
            records1.set_value(index, 'mktoLeadOwnerFullname', str(item["mktoLeadOwnerFullname"]))
            records1.set_value(index, 'SalesPredict_AWS__c', str(item["SalesPredict_AWS__c"]))
            records1.set_value(index, 'Legacy_User__c', str(item["Legacy_User__c"]))
            records1.set_value(index, 'SD_Company_Name__c', str(item["SD_Company_Name__c"]))
            records1.set_value(index, 'Preferred_Language__c', str(item["Preferred_Language__c"]))
            records1.set_value(index, 'Top_Priority__c', str(item["Top_Priority__c"]))
            records1.set_value(index, 'Top_Customer__c', str(item["Top_Customer__c"]))
            records1.set_value(index, 'SDR__c', str(item["SDR__c"]))
            records1.set_value(index, 'behavior_Score_at_MQL', str(item["behavior_Score_at_MQL"]))
            records1.set_value(index, 'predictive_Rank_at_MQL', str(item["predictive_Rank_at_MQL"]))
            records1.set_value(index, 'lead_Score_at_MQL', str(item["lead_Score_at_MQL"]))
            records1.set_value(index, 'SalesPredict_Score_at_MQL', str(item["SalesPredict_Score_at_MQL"]))
            records1.set_value(index, 'sSMatched', str(item["sSMatched"]))
            records1.set_value(index, 'sSNotMatched', str(item["sSNotMatched"]))
            records1.set_value(index, 'Contact_License_Mismatch__c', str(item["Contact_License_Mismatch__c"]))
            records1.set_value(index, 'SDR_Email__c', str(item["SDR_Email__c"]))
            records1.set_value(index, 'Converted_to_Opportunity__c', str(item["Converted_to_Opportunity__c"]))
            records1.set_value(index, 'Contact_License_Mismatch_reseller__c',
                               str(item["Contact_License_Mismatch_reseller__c"]))
            records1.set_value(index, 'Converted_to_ContactC__c', str(item["Converted_to_ContactC__c"]))
            records1.set_value(index, 'X1_Inquiry_date__c', str(item["X1_Inquiry_date__c"]))
            records1.set_value(index, 'X2_Ready_for_Review_Date__c', str(item["X2_Ready_for_Review_Date__c"]))
            records1.set_value(index, 'X3_Working_Date__c', str(item["X3_Working_Date__c"]))
            records1.set_value(index, 'X4_Qualifying_Date__c', str(item["X4_Qualifying_Date__c"]))
            records1.set_value(index, 'X5_Qualified_Date__c', str(item["X5_Qualified_Date__c"]))
            records1.set_value(index, 'X6_Recycle_Date__c', str(item["X6_Recycle_Date__c"]))
            records1.set_value(index, 'X7_Do_Not_Contact_Date__c', str(item["X7_Do_Not_Contact_Date__c"]))
            records1.set_value(index, 'Acquisition_Asset_Type__c', str(item["Acquisition_Asset_Type__c"]))
            records1.set_value(index, 'Acquisition_Campaign__c', str(item["Acquisition_Campaign__c"]))
            records1.set_value(index, 'MQL_Asset_Type__c', str(item["MQL_Asset_Type__c"]))
            records1.set_value(index, 'MQL_Campaign__c', str(item["MQL_Campaign__c"]))
            records1.set_value(index, 'End_User_Contact__c', str(item["End_User_Contact__c"]))
            records1.set_value(index, 'Decision_Maker_Contact__c', str(item["Decision_Maker_Contact__c"]))
            records1.set_value(index, 'Linked_Account__c', str(item["Linked_Account__c"]))
            records1.set_value(index, 'LeanData__A2B_Account__c', str(item["LeanData__A2B_Account__c"]))
            records1.set_value(index, 'LeanData__A2B_Group__c', str(item["LeanData__A2B_Group__c"]))
            records1.set_value(index, 'LeanData__Has_Matched__c', str(item["LeanData__Has_Matched__c"]))
            records1.set_value(index, 'LeanData__Marketing_Sys_Created_Date__c',
                               str(item["LeanData__Marketing_Sys_Created_Date__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Annual_Revenue__c',
                               str(item["LeanData__Matched_Account_Annual_Revenue__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Billing_Country__c',
                               str(item["LeanData__Matched_Account_Billing_Country__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Billing_Postal_Code__c',
                               str(item["LeanData__Matched_Account_Billing_Postal_Code__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Billing_State__c',
                               str(item["LeanData__Matched_Account_Billing_State__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Custom_Field_1__c',
                               str(item["LeanData__Matched_Account_Custom_Field_1__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Employees__c',
                               str(item["LeanData__Matched_Account_Employees__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Industry__c',
                               str(item["LeanData__Matched_Account_Industry__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Name__c',
                               str(item["LeanData__Matched_Account_Name__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Type__c',
                               str(item["LeanData__Matched_Account_Type__c"]))
            records1.set_value(index, 'LeanData__Matched_Account_Website__c',
                               str(item["LeanData__Matched_Account_Website__c"]))
            records1.set_value(index, 'LeanData__Matched_Account__c', str(item["LeanData__Matched_Account__c"]))
            records1.set_value(index, 'LeanData__Matched_Buyer_Persona__c',
                               str(item["LeanData__Matched_Buyer_Persona__c"]))
            records1.set_value(index, 'LeanData__Matched_Lead__c', str(item["LeanData__Matched_Lead__c"]))
            records1.set_value(index, 'LeanData__Reporting_Matched_Account__c',
                               str(item["LeanData__Reporting_Matched_Account__c"]))
            records1.set_value(index, 'LeanData__Reporting_Timestamp__c',
                               str(item["LeanData__Reporting_Timestamp__c"]))
            records1.set_value(index, 'LeanData__Router_Status__c', str(item["LeanData__Router_Status__c"]))
            records1.set_value(index, 'LeanData__Routing_Action__c', str(item["LeanData__Routing_Action__c"]))
            records1.set_value(index, 'LeanData__Routing_Status__c', str(item["LeanData__Routing_Status__c"]))
            records1.set_value(index, 'LeanData__Salesforce_Id__c', str(item["LeanData__Salesforce_Id__c"]))
            records1.set_value(index, 'LeanData__Search_Index__c', str(item["LeanData__Search_Index__c"]))
            records1.set_value(index, 'LeanData__Search__c', str(item["LeanData__Search__c"]))
            records1.set_value(index, 'LeanData__Segment__c', str(item["LeanData__Segment__c"]))
            records1.set_value(index, 'LeanData__Status_Info__c', str(item["LeanData__Status_Info__c"]))
            records1.set_value(index, 'LeanData__Tag__c', str(item["LeanData__Tag__c"]))
            records1.set_value(index, 'LeanData__LD_EmailDomain__c', str(item["LeanData__LD_EmailDomain__c"]))
            records1.set_value(index, 'LeanData__LD_EmailDomains__c', str(item["LeanData__LD_EmailDomains__c"]))
            records1.set_value(index, 'LeanData__Reporting_Customer__c',
                               str(item["LeanData__Reporting_Customer__c"]))
            records1.set_value(index, 'LeanData__Reporting_Has_Opportunity__c',
                               str(item["LeanData__Reporting_Has_Opportunity__c"]))
            records1.set_value(index, 'LeanData__Reporting_Last_Marketing_Touch_Date__c',
                               str(item["LeanData__Reporting_Last_Marketing_Touch_Date__c"]))
            records1.set_value(index, 'LeanData__Reporting_Last_Sales_Touch_Date__c',
                               str(item["LeanData__Reporting_Last_Sales_Touch_Date__c"]))
            records1.set_value(index, 'LeanData__Reporting_Recent_Marketing_Touches__c',
                               str(item["LeanData__Reporting_Recent_Marketing_Touches__c"]))
            records1.set_value(index, 'LeanData__Reporting_Target_Account_Number__c',
                               str(item["LeanData__Reporting_Target_Account_Number__c"]))
            records1.set_value(index, 'LeanData__Reporting_Target_Account__c',
                               str(item["LeanData__Reporting_Target_Account__c"]))
            records1.set_value(index, 'LeanData__Reporting_Total_Leads_and_Contacts__c',
                               str(item["LeanData__Reporting_Total_Leads_and_Contacts__c"]))
            records1.set_value(index, 'LeanData__Reporting_Total_Marketing_Touches__c',
                               str(item["LeanData__Reporting_Total_Marketing_Touches__c"]))
            records1.set_value(index, 'LeanData__SLA__c', str(item["LeanData__SLA__c"]))
            records1.set_value(index, 'LeanData__Scenario_1_Owner__c', str(item["LeanData__Scenario_1_Owner__c"]))
            records1.set_value(index, 'LeanData__Scenario_2_Owner__c', str(item["LeanData__Scenario_2_Owner__c"]))
            records1.set_value(index, 'LeanData__Scenario_3_Owner__c', str(item["LeanData__Scenario_3_Owner__c"]))
            records1.set_value(index, 'LeanData__Scenario_4_Owner__c', str(item["LeanData__Scenario_4_Owner__c"]))
            records1.set_value(index, 'LeanData__Search__c_account', str(item["LeanData__Search__c_account"]))
            records1.set_value(index, 'LeanData__Tag__c_account', str(item["LeanData__Tag__c_account"]))
            records1.set_value(index, 'Convert_to_Contact__c', str(item["Convert_to_Contact__c"]))
            records1.set_value(index, 'BigDataSandbox', str(item["BigDataSandbox"]))
            records1.set_value(index, 'DSCORGPKG__CUSTOM_COUNTRY__c', str(item["DSCORGPKG__CUSTOM_COUNTRY__c"]))
            records1.set_value(index, 'DSCORGPKG__CUSTOM_STATE__c', str(item["DSCORGPKG__CUSTOM_STATE__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Annual_Rev__c',
                               str(item["DSCORGPKG__Custom_Annual_Rev__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Company_HQ__c',
                               str(item["DSCORGPKG__Custom_Company_HQ__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Emp_No__c', str(item["DSCORGPKG__Custom_Emp_No__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Fiscal_Year__c',
                               str(item["DSCORGPKG__Custom_Fiscal_Year__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_ITBudget__c', str(item["DSCORGPKG__Custom_ITBudget__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_ITEmp_c__c', str(item["DSCORGPKG__Custom_ITEmp_c__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_LinkedUrl__c', str(item["DSCORGPKG__Custom_LinkedUrl__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Title__c', str(item["DSCORGPKG__Custom_Title__c"]))
            records1.set_value(index, 'DSCORGPKG__Locked_By_User__c', str(item["DSCORGPKG__Locked_By_User__c"]))
            records1.set_value(index, 'DSCORGPKG__Cust_Fiscal_Year__c', str(item["DSCORGPKG__Cust_Fiscal_Year__c"]))
            records1.set_value(index, 'DSCORGPKG__Cust_IT_Budget__c', str(item["DSCORGPKG__Cust_IT_Budget__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_3yr__c', str(item["DSCORGPKG__Custom_3yr__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Country_Full_RA__c',
                               str(item["DSCORGPKG__Custom_Country_Full_RA__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Country_RA__c',
                               str(item["DSCORGPKG__Custom_Country_RA__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_DUNS__c', str(item["DSCORGPKG__Custom_DUNS__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Emp_No__c_account',
                               str(item["DSCORGPKG__Custom_Emp_No__c_account"]))
            records1.set_value(index, 'DSCORGPKG__Custom_ITEmp__c', str(item["DSCORGPKG__Custom_ITEmp__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_NOA__c', str(item["DSCORGPKG__Custom_NOA__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Revenue__c', str(item["DSCORGPKG__Custom_Revenue__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_State_Full_RA__c',
                               str(item["DSCORGPKG__Custom_State_Full_RA__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_State_RA__c', str(item["DSCORGPKG__Custom_State_RA__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_des__c', str(item["DSCORGPKG__Custom_des__c"]))
            records1.set_value(index, 'DSCORGPKG__Locked_By_User__c_account',
                               str(item["DSCORGPKG__Locked_By_User__c_account"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Address__c', str(item["DSCORGPKG__Custom_Address__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Company_HQ_Address__c',
                               str(item["DSCORGPKG__Custom_Company_HQ_Address__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Company_HQ_City__c',
                               str(item["DSCORGPKG__Custom_Company_HQ_City__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Country__c_contact',
                               str(item["DSCORGPKG__Custom_Country__c_contact"]))
            records1.set_value(index, 'DSCORGPKG__Custom_Phone__c', str(item["DSCORGPKG__Custom_Phone__c"]))
            records1.set_value(index, 'DSCORGPKG__Custom_State__c_contact',
                               str(item["DSCORGPKG__Custom_State__c_contact"]))
            records1.set_value(index, 'DSCORGPKG__REMOVELinkedinURL__c',
                               str(item["DSCORGPKG__REMOVELinkedinURL__c"]))
            records1.set_value(index, 'DSCORGPKG__title_Custom__c', str(item["DSCORGPKG__title_Custom__c"]))
            records1.set_value(index, 'Talend_6_x__c', str(item["Talend_6_x__c"]))
            records1.set_value(index, 'Puchase_Influence_Level__c', str(item["Puchase_Influence_Level__c"]))
            records1.set_value(index, 'Author__c', str(item["Author__c"]))
            records1.set_value(index, 'Survey_Language_Code__c', str(item["Survey_Language_Code__c"]))
            records1.set_value(index, 'CSM_User__c', str(item["CSM_User__c"]))
            records1.set_value(index, 'Current_Product_Version__c', str(item["Current_Product_Version__c"]))
            records1.set_value(index, 'Follow_up_Escalation_Owner_1__c',
                               str(item["Follow_up_Escalation_Owner_1__c"]))
            records1.set_value(index, 'Market__c', str(item["Market__c"]))
            records1.set_value(index, 'Product_Name__c', str(item["Product_Name__c"]))
            records1.set_value(index, 'Professional_Services__c', str(item["Professional_Services__c"]))
            records1.set_value(index, 'Software_Upgrade__c', str(item["Software_Upgrade__c"]))
            records1.set_value(index, 'Future_Theater__c', str(item["Future_Theater__c"]))
            records1.set_value(index, 'Survey_Language_Code__c_contact',
                               str(item["Survey_Language_Code__c_contact"]))
            records1.set_value(index, 'Renewal_Check__c', str(item["Renewal_Check__c"]))
            records1.set_value(index, 'NPS_Check__c', str(item["NPS_Check__c"]))
            records1.set_value(index, 'Purchase_Influence_Level__c', str(item["Purchase_Influence_Level__c"]))
            records1.set_value(index, 'Check__c', str(item["Check__c"]))
            records1.set_value(index, 'Response_Rate_Notification_Recipient__c',
                               str(item["Response_Rate_Notification_Recipient__c"]))
            records1.set_value(index, 'PrimaryScore__c', str(item["PrimaryScore__c"]))
            records1.set_value(index, 'AVA__AVAAI_action_required__c', str(item["AVA__AVAAI_action_required__c"]))
            records1.set_value(index, 'AVA__AVAAI_action_required_date__c',
                               str(item["AVA__AVAAI_action_required_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_conversation_stage__c',
                               str(item["AVA__AVAAI_conversation_stage__c"]))
            records1.set_value(index, 'AVA__AVAAI_conversation_stage_date__c',
                               str(item["AVA__AVAAI_conversation_stage_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_conversation_status__c',
                               str(item["AVA__AVAAI_conversation_status__c"]))
            records1.set_value(index, 'AVA__AVAAI_conversation_status_date__c',
                               str(item["AVA__AVAAI_conversation_status_date__c"]))
            records1.set_value(index, 'AVA__AVAAI_conversica_lead_status__c',
                               str(item["AVA__AVAAI_conversica_lead_status__c"]))
            records1.set_value(index, 'AVA__AVAAI_conversica_lead_status_date__c',
                               str(item["AVA__AVAAI_conversica_lead_status_date__c"]))
            records1.set_value(index, 'cas__FirstAttempt__c', str(item["cas__FirstAttempt__c"]))
            records1.set_value(index, 'cas__First_Conversation_Date__c',
                               str(item["cas__First_Conversation_Date__c"]))
            records1.set_value(index, 'cas__LastAttempt__c', str(item["cas__LastAttempt__c"]))
            records1.set_value(index, 'cas__Last_Connect__c', str(item["cas__Last_Connect__c"]))
            records1.set_value(index, 'cas__List_Name__c', str(item["cas__List_Name__c"]))
            records1.set_value(index, 'cas__Most_Recent_Attempt_Disposition__c',
                               str(item["cas__Most_Recent_Attempt_Disposition__c"]))
            records1.set_value(index, 'cas__Most_Recent_Conversation_Disposition__c',
                               str(item["cas__Most_Recent_Conversation_Disposition__c"]))
            records1.set_value(index, 'cas__Most_Recent_Disposition__c',
                               str(item["cas__Most_Recent_Disposition__c"]))
            records1.set_value(index, 'cas__NumberAttempts__c', str(item["cas__NumberAttempts__c"]))
            records1.set_value(index, 'cas__NumberConnects__c', str(item["cas__NumberConnects__c"]))
            records1.set_value(index, 'cas__Penalty_Box_Status__c', str(item["cas__Penalty_Box_Status__c"]))
            records1.set_value(index, 'cas__ContactStatus__c', str(item["cas__ContactStatus__c"]))
            records1.set_value(index, 'Author_for_Opportunity__c', str(item["Author_for_Opportunity__c"]))
            records1.set_value(index, 'NS_Account_Number__c', str(item["NS_Account_Number__c"]))
            records1.set_value(index, 'Partner_portal_sourced__c', str(item["Partner_portal_sourced__c"]))
            records1.set_value(index, 'Partner_portal_sourced__c_account',
                               str(item["Partner_portal_sourced__c_account"]))
            records1.set_value(index, 'Ctvt_CloseDate__c', str(item["Ctvt_CloseDate__c"]))
            records1.set_value(index, 'PartnerPortalSourced__c', str(item["PartnerPortalSourced__c"]))
            records1.set_value(index, 'Lattice_Score__c', str(item["Lattice_Score__c"]))
            records1.set_value(index, 'Lattice_Timestamp__c', str(item["Lattice_Timestamp__c"]))
            records1.set_value(index, 'Lattice_Webhook_Timestamp__c', str(item["Lattice_Webhook_Timestamp__c"]))
            records1.set_value(index, 'Ctvt_PartnerOrgName__c', str(item["Ctvt_PartnerOrgName__c"]))
            records1.set_value(index, 'Ctvt_PartnerUserEmail__c', str(item["Ctvt_PartnerUserEmail__c"]))
            records1.set_value(index, 'Ctvt_CurrencyOfTheOpportunity_1_1__c',
                               str(item["Ctvt_CurrencyOfTheOpportunity_1_1__c"]))
            records1.set_value(index, 'Ctvt_Amount__c', str(item["Ctvt_Amount__c"]))
            records1.set_value(index, 'Ctvt_RegistrationStatus_1__c', str(item["Ctvt_RegistrationStatus_1__c"]))
            records1.set_value(index, 'Ctvt_PartnerUserName__c', str(item["Ctvt_PartnerUserName__c"]))
            records1.set_value(index, 'Ctvt_Stage__c', str(item["Ctvt_Stage__c"]))
            records1.set_value(index, 'Ctvt_Title__c', str(item["Ctvt_Title__c"]))
            records1.set_value(index, 'Ctvt_ProjectBudgetInLocalCurrency_1__c',
                               str(item["Ctvt_ProjectBudgetInLocalCurrency_1__c"]))
            records1.set_value(index, 'Ctvt_PartnerUserPhone__c', str(item["Ctvt_PartnerUserPhone__c"]))
            records1.set_value(index, 'Ctvt_TimelineOtherDatesAndDeadlines_1__c',
                               str(item["Ctvt_TimelineOtherDatesAndDeadlines_1__c"]))
            records1.set_value(index, 'Ctvt_SummaryOfTheTechnicalEnvironme_1__c',
                               str(item["Ctvt_SummaryOfTheTechnicalEnvironme_1__c"]))
            records1.set_value(index, 'Ctvt_Sys_EntityType__c', str(item["Ctvt_Sys_EntityType__c"]))
            records1.set_value(index, 'Ctvt_Sys_URL__c', str(item["Ctvt_Sys_URL__c"]))
            records1.set_value(index, 'Ctvt_HowCanTalendHelpYouWithYourCus_1__c',
                               str(item["Ctvt_HowCanTalendHelpYouWithYourCus_1__c"]))
            records1.set_value(index, 'Ctvt_Sys_LastUpdated__c', str(item["Ctvt_Sys_LastUpdated__c"]))
            records1.set_value(index, 'Ctvt_CurrentEngagementWithTheCustom_1__c',
                               str(item["Ctvt_CurrentEngagementWithTheCustom_1__c"]))
            records1.set_value(index, 'Ctvt_EngagementHistoryWithTheCustom_1__c',
                               str(item["Ctvt_EngagementHistoryWithTheCustom_1__c"]))
            records1.set_value(index, 'Ctvt_AnyOtherInformation_1__c', str(item["Ctvt_AnyOtherInformation_1__c"]))
            records1.set_value(index, 'Ctvt_SummaryOfTheDealopportunityKey_1__c',
                               str(item["Ctvt_SummaryOfTheDealopportunityKey_1__c"]))
            records1.set_value(index, 'Ctvt_DidYouTalkToATalendRepIfSoPlea_1__c',
                               str(item["Ctvt_DidYouTalkToATalendRepIfSoPlea_1__c"]))
            records1.set_value(index, 'LBI__EstimatedRevenue__c', str(item["LBI__EstimatedRevenue__c"]))
            records1.set_value(index, 'LBI__LatticeRating__c', str(item["LBI__LatticeRating__c"]))
            records1.set_value(index, 'LBI__Recommendation__c', str(item["LBI__Recommendation__c"]))
            records1.set_value(index, 'LBI__AccountExtension__c', str(item["LBI__AccountExtension__c"]))
            records1.set_value(index, 'LBI__NumberOfOpenInProgressRecommendations__c',
                               str(item["LBI__NumberOfOpenInProgressRecommendations__c"]))
            records1.set_value(index, 'LBI__AccountName__c', str(item["LBI__AccountName__c"]))
            records1.set_value(index, 'Lattice_Rank__c', str(item["Lattice_Rank__c"]))
            records1.set_value(index, 'jobFunction2', str(item["jobFunction2"]))
            records1.set_value(index, 'Critical_Account__c', str(item["Critical_Account__c"]))
            records1.set_value(index, 'NPS_Check_Accts_up_for_Renewal__c',
                               str(item["NPS_Check_Accts_up_for_Renewal__c"]))
            records1.set_value(index, 'Quarter__c', str(item["Quarter__c"]))
            records1.set_value(index, 'Today_s_Quarter__c', str(item["Today_s_Quarter__c"]))
            records1.set_value(index, 'cventJobTitle', str(item["cventJobTitle"]))
            records1.set_value(index, 'cventAdmissionItem', str(item["cventAdmissionItem"]))
            records1.set_value(index, 'cventRegistrationType', str(item["cventRegistrationType"]))
            records1.set_value(index, 'cventRegistrationStatus', str(item["cventRegistrationStatus"]))
            records1.set_value(index, 'cventConfirmation', str(item["cventConfirmation"]))
            records1.set_value(index, 'cventRegistrationDate', str(item["cventRegistrationDate"]))
            records1.set_value(index, 'Ctvt_Description_1__c', str(item["Ctvt_Description_1__c"]))
            records1.set_value(index, 'Ctvt_AnyOtherInformation_2__c', str(item["Ctvt_AnyOtherInformation_2__c"]))
            records1.set_value(index, 'Sales_Activities_Since_Last_MQL__c',
                               str(item["Sales_Activities_Since_Last_MQL__c"]))
            records1.set_value(index, 'Latitude', str(item["Latitude"]))
            records1.set_value(index, 'Longitude', str(item["Longitude"]))
            records1.set_value(index, 'GeocodeAccuracy', str(item["GeocodeAccuracy"]))
            records1.set_value(index, 'Address', str(item["Address"]))
            records1.set_value(index, 'PhotoUrl', str(item["PhotoUrl"]))
            records1.set_value(index, 'LastViewedDate', str(item["LastViewedDate"]))
            records1.set_value(index, 'LastReferencedDate', str(item["LastReferencedDate"]))
            records1.set_value(index, 'JigsawContactId_lead', str(item["JigsawContactId_lead"]))
            records1.set_value(index, 'CleanStatus', str(item["CleanStatus"]))
            records1.set_value(index, 'CompanyDunsNumber', str(item["CompanyDunsNumber"]))
            records1.set_value(index, 'BillingLatitude', str(item["BillingLatitude"]))
            records1.set_value(index, 'BillingLongitude', str(item["BillingLongitude"]))
            records1.set_value(index, 'BillingGeocodeAccuracy', str(item["BillingGeocodeAccuracy"]))
            records1.set_value(index, 'BillingAddress', str(item["BillingAddress"]))
            records1.set_value(index, 'ShippingLatitude', str(item["ShippingLatitude"]))
            records1.set_value(index, 'ShippingLongitude', str(item["ShippingLongitude"]))
            records1.set_value(index, 'ShippingGeocodeAccuracy', str(item["ShippingGeocodeAccuracy"]))
            records1.set_value(index, 'ShippingAddress', str(item["ShippingAddress"]))
            records1.set_value(index, 'PhotoUrl_account', str(item["PhotoUrl_account"]))
            records1.set_value(index, 'LastViewedDate_account', str(item["LastViewedDate_account"]))
            records1.set_value(index, 'LastReferencedDate_account', str(item["LastReferencedDate_account"]))
            records1.set_value(index, 'JigsawCompanyId_account', str(item["JigsawCompanyId_account"]))
            records1.set_value(index, 'CleanStatus_account', str(item["CleanStatus_account"]))
            records1.set_value(index, 'AccountSource', str(item["AccountSource"]))
            records1.set_value(index, 'DunsNumber', str(item["DunsNumber"]))
            records1.set_value(index, 'Tradestyle', str(item["Tradestyle"]))
            records1.set_value(index, 'NaicsCode', str(item["NaicsCode"]))
            records1.set_value(index, 'NaicsDesc', str(item["NaicsDesc"]))
            records1.set_value(index, 'YearStarted', str(item["YearStarted"]))
            records1.set_value(index, 'SicDesc', str(item["SicDesc"]))
            records1.set_value(index, 'OtherLatitude', str(item["OtherLatitude"]))
            records1.set_value(index, 'OtherLongitude', str(item["OtherLongitude"]))
            records1.set_value(index, 'OtherGeocodeAccuracy', str(item["OtherGeocodeAccuracy"]))
            records1.set_value(index, 'OtherAddress', str(item["OtherAddress"]))
            records1.set_value(index, 'MailingLatitude', str(item["MailingLatitude"]))
            records1.set_value(index, 'MailingLongitude', str(item["MailingLongitude"]))
            records1.set_value(index, 'MailingGeocodeAccuracy', str(item["MailingGeocodeAccuracy"]))
            records1.set_value(index, 'MailingAddress', str(item["MailingAddress"]))
            records1.set_value(index, 'IsEmailBounced', str(item["IsEmailBounced"]))
            records1.set_value(index, 'Ctvt_AdditionalInformation_1__c',
                               str(item["Ctvt_AdditionalInformation_1__c"]))
            records1.set_value(index, 'Ctvt_HowCanTalendAssistYouWithYourC__c',
                               str(item["Ctvt_HowCanTalendAssistYouWithYourC__c"]))
            records1.set_value(index, 'LIM_since_Recycle__c', str(item["LIM_since_Recycle__c"]))
            records1.set_value(index, 'leadCodeCustom', str(item["leadCodeCustom"]))
            records1.set_value(index, 'First_Activity__c', str(item["First_Activity__c"]))
            records1.set_value(index, 'Lattice_Behavioral_Score__c', str(item["Lattice_Behavioral_Score__c"]))
            records1.set_value(index, 'Lattice_Behavioral_Timestamp__c',
                               str(item["Lattice_Behavioral_Timestamp__c"]))
            records1.set_value(index, 'Lattice_Behavioral_Rating__c', str(item["Lattice_Behavioral_Rating__c"]))
            records1.set_value(index, 'Assigned_CSMs__c', str(item["Assigned_CSMs__c"]))
            records1.set_value(index, 'Lattice_Fit_Behavior__c', str(item["Lattice_Fit_Behavior__c"]))
            records1.set_value(index, 'Lattice_Fit_Behavior_Timestamp__c',
                               str(item["Lattice_Fit_Behavior_Timestamp__c"]))
            records1.set_value(index, 'Awareness_Campaign_Sent__c', str(item["Awareness_Campaign_Sent__c"]))
            records1.set_value(index, 'DP_included_in_on_boarding__c', str(item["DP_included_in_on_boarding__c"]))
            records1.set_value(index, 'Info_Requested__c', str(item["Info_Requested__c"]))
            records1.set_value(index, 'Demo_Requested__c', str(item["Demo_Requested__c"]))
            records1.set_value(index, 'POC_Requested__c', str(item["POC_Requested__c"]))
            records1.set_value(index, 'Free_Licenses_activated__c', str(item["Free_Licenses_activated__c"]))
            records1.set_value(index, 'DP_in_Prod_Use__c', str(item["DP_in_Prod_Use__c"]))
            records1.set_value(index, 'rrpu__Alert_Message__c', str(item["rrpu__Alert_Message__c"]))
            records1.set_value(index, 'rrpu__Alert_Message__c_account', str(item["rrpu__Alert_Message__c_account"]))
            records1.set_value(index, 'LPI_Cloud_Infrastructure_Tech__c',
                               str(item["LPI_Cloud_Infrastructure_Tech__c"]))
            records1.set_value(index, 'LPI_Cloud_Service_Tier_1__c', str(item["LPI_Cloud_Service_Tier_1__c"]))
            records1.set_value(index, 'LPI_Cloud_Service_Tier_2__c', str(item["LPI_Cloud_Service_Tier_2__c"]))
            records1.set_value(index, 'LBI_Cloud_Infrastructure_Tech__c',
                               str(item["LBI_Cloud_Infrastructure_Tech__c"]))
            records1.set_value(index, 'LBI_Cloud_Service_Tier_1__c', str(item["LBI_Cloud_Service_Tier_1__c"]))
            records1.set_value(index, 'LBI_Cloud_Service_Tier_2__c', str(item["LBI_Cloud_Service_Tier_2__c"]))
            records1.set_value(index, 'LPI_Has_Adobe_Target_Standard__c',
                               str(item["LPI_Has_Adobe_Target_Standard__c"]))
            records1.set_value(index, 'LPI_Has_Amazon_AWS__c', str(item["LPI_Has_Amazon_AWS__c"]))
            records1.set_value(index, 'LBI_Has_Amazon_Redshift__c', str(item["LBI_Has_Amazon_Redshift__c"]))
            records1.set_value(index, 'LPI_Has_Apache_Hadoop__c', str(item["LPI_Has_Apache_Hadoop__c"]))
            records1.set_value(index, 'LBI_Has_Apache_Hive__c', str(item["LBI_Has_Apache_Hive__c"]))
            records1.set_value(index, 'LBI_Has_Cloudera__c', str(item["LBI_Has_Cloudera__c"]))
            records1.set_value(index, 'LBI_Has_CoolaData__c', str(item["LBI_Has_CoolaData__c"]))
            records1.set_value(index, 'LBI_Has_IBM_InfoSphere_DataStage__c',
                               str(item["LBI_Has_IBM_InfoSphere_DataStage__c"]))
            records1.set_value(index, 'LBI_Has_Informatica__c', str(item["LBI_Has_Informatica__c"]))
            records1.set_value(index, 'LBI_Has_Loggly__c', str(item["LBI_Has_Loggly__c"]))
            records1.set_value(index, 'LBI_Has_Mulesoft__c', str(item["LBI_Has_Mulesoft__c"]))
            records1.set_value(index, 'LBI_Has_Rekko__c', str(item["LBI_Has_Rekko__c"]))
            records1.set_value(index, 'LBI_Has_TellApart__c', str(item["LBI_Has_TellApart__c"]))
            records1.set_value(index, 'LBI_Has_Adobe_Target_Standard__c',
                               str(item["LBI_Has_Adobe_Target_Standard__c"]))
            records1.set_value(index, 'LBI_Has_Amazon_AWS__c', str(item["LBI_Has_Amazon_AWS__c"]))
            records1.set_value(index, 'LBI_Has_Apache_Hadoop__c', str(item["LBI_Has_Apache_Hadoop__c"]))
            records1.set_value(index, 'Express_Consent__c', str(item["Express_Consent__c"]))
            records1.set_value(index, 'Express_Consent_History__c', str(item["Express_Consent_History__c"]))
            records1.set_value(index, 'Inferred_Consent__c', str(item["Inferred_Consent__c"]))
            records1.set_value(index, 'Inferred_Consent_History__c', str(item["Inferred_Consent_History__c"]))
            records1.set_value(index, 'Created_By_Role__c', str(item["Created_By_Role__c"]))
            records1.set_value(index, 'Global_Account__c', str(item["Global_Account__c"]))
            records1.set_value(index, 'Regional_AE__c', str(item["Regional_AE__c"]))
            records1.set_value(index, 'First_MQL_Date__c', str(item["First_MQL_Date__c"]))
            records1.set_value(index, 'Not_Interested__c', str(item["Not_Interested__c"]))
            records1.set_value(index, 'Date_of_Last_Data_Prep_Conversation__c',
                               str(item["Date_of_Last_Data_Prep_Conversation__c"]))
            records1.set_value(index, 'Active_User_Status__c', str(item["Active_User_Status__c"]))
            records1.set_value(index, 'temp_assignment', str(item["temp_assignment"]))
            records1.set_value(index, 'Ctvt_RenewalOpportunity__c', str(item["Ctvt_RenewalOpportunity__c"]))
            records1.set_value(index, 'Ctvt_BrandNewOpportunity__c', str(item["Ctvt_BrandNewOpportunity__c"]))
            records1.set_value(index, 'Chat_Transcript__c', str(item["Chat_Transcript__c"]))
            records1.set_value(index, 'Chat_Agent_ID__c', str(item["Chat_Agent_ID__c"]))
            records1.set_value(index, 'Payment_Term__c', str(item["Payment_Term__c"]))
            records1.set_value(index, 'Customer_Acquisition_Date__c', str(item["Customer_Acquisition_Date__c"]))
            records1.set_value(index, 'Account_ID_long__c', str(item["Account_ID_long__c"]))
            records1.set_value(index, 'LMS_Student_ID__c', str(item["LMS_Student_ID__c"]))
            records1.set_value(index, 'Actual_Users__c', str(item["Actual_Users__c"]))
            records1.set_value(index, 'Are_you_using_Joblets__c', str(item["Are_you_using_Joblets__c"]))
            records1.set_value(index, 'Big_Data_Components__c', str(item["Big_Data_Components__c"]))
            records1.set_value(index, 'Big_Data_Streaming_in_Use__c', str(item["Big_Data_Streaming_in_Use__c"]))
            records1.set_value(index, 'Building_Actions__c', str(item["Building_Actions__c"]))
            records1.set_value(index, 'Building_Map_Reduce_of_Spark_Batch_Jobs__c',
                               str(item["Building_Map_Reduce_of_Spark_Batch_Jobs__c"]))
            records1.set_value(index, 'Building_Mediation_Routes__c', str(item["Building_Mediation_Routes__c"]))
            records1.set_value(index, 'Building_SOAP_or_REST_Services__c',
                               str(item["Building_SOAP_or_REST_Services__c"]))
            records1.set_value(index, 'Building_a_Lambda_Kappa_Zeta_Arch__c',
                               str(item["Building_a_Lambda_Kappa_Zeta_Arch__c"]))
            records1.set_value(index, 'Cloud_Environment__c', str(item["Cloud_Environment__c"]))
            records1.set_value(index, 'Completed_Training__c', str(item["Completed_Training__c"]))
            records1.set_value(index, 'DEV__c', str(item["DEV__c"]))
            records1.set_value(index, 'Data_Cleansing_Masking_Used__c', str(item["Data_Cleansing_Masking_Used__c"]))
            records1.set_value(index, 'Database_Type__c', str(item["Database_Type__c"]))
            records1.set_value(index, 'Develop_Using_Spring_DLS__c', str(item["Develop_Using_Spring_DLS__c"]))
            records1.set_value(index, 'Disaster_Recovery__c', str(item["Disaster_Recovery__c"]))
            records1.set_value(index, 'EOL_12_months__c', str(item["EOL_12_months__c"]))
            records1.set_value(index, 'Engaged__c', str(item["Engaged__c"]))
            records1.set_value(index, 'Finite_Project__c', str(item["Finite_Project__c"]))
            records1.set_value(index, 'Hadoop_Components_Used__c', str(item["Hadoop_Components_Used__c"]))
            records1.set_value(index, 'How_many_data_stewards__c', str(item["How_many_data_stewards__c"]))
            records1.set_value(index, 'Implementation_Approach__c', str(item["Implementation_Approach__c"]))
            records1.set_value(index, 'Implementation__c', str(item["Implementation__c"]))
            records1.set_value(index, 'In_Production__c', str(item["In_Production__c"]))
            records1.set_value(index, 'Java_Version__c', str(item["Java_Version__c"]))
            records1.set_value(index, 'MDMs_Driving_Critical_Business_Processes__c',
                               str(item["MDMs_Driving_Critical_Business_Processes__c"]))
            records1.set_value(index, 'Open_Feature_Request__c', str(item["Open_Feature_Request__c"]))
            records1.set_value(index, 'Operating_System__c', str(item["Operating_System__c"]))
            records1.set_value(index, 'Pre_Production__c', str(item["Pre_Production__c"]))
            records1.set_value(index, 'Product_Deployed_in_the_Cloud__c',
                               str(item["Product_Deployed_in_the_Cloud__c"]))
            records1.set_value(index, 'Production__c', str(item["Production__c"]))
            records1.set_value(index, 'Referenceable__c', str(item["Referenceable__c"]))
            records1.set_value(index, 'System_Integration_Test__c', str(item["System_Integration_Test__c"]))
            records1.set_value(index, 'TAC_Users__c', str(item["TAC_Users__c"]))
            records1.set_value(index, 'TEST__c', str(item["TEST__c"]))
            records1.set_value(index, 'User_Acceptance_Test__c', str(item["User_Acceptance_Test__c"]))
            records1.set_value(index, 'Using_All_Licenses__c', str(item["Using_All_Licenses__c"]))
            records1.set_value(index, 'Using_All_Products__c', str(item["Using_All_Products__c"]))
            records1.set_value(index, 'Using_Big_Data_Components__c', str(item["Using_Big_Data_Components__c"]))
            records1.set_value(index, 'Using_ML_Algorithms_or_Components__c',
                               str(item["Using_ML_Algorithms_or_Components__c"]))
            records1.set_value(index, 'Using_Metadata_Bridge__c', str(item["Using_Metadata_Bridge__c"]))
            records1.set_value(index, 'Using_Profiling_features_of_the_Studio__c',
                               str(item["Using_Profiling_features_of_the_Studio__c"]))
            records1.set_value(index, 'Using_Spark_Streaming__c', str(item["Using_Spark_Streaming__c"]))
            records1.set_value(index, 'Using_TAC_in_Development__c', str(item["Using_TAC_in_Development__c"]))
            records1.set_value(index, 'Using_TAC_in_High_Availability__c',
                               str(item["Using_TAC_in_High_Availability__c"]))
            records1.set_value(index, 'Using_TAC_in_Production__c', str(item["Using_TAC_in_Production__c"]))
            records1.set_value(index, 'Using_Talend_Data_Mapper__c', str(item["Using_Talend_Data_Mapper__c"]))
            records1.set_value(index, 'Using_Talend_Data_Prep_2_Free_Licenses__c',
                               str(item["Using_Talend_Data_Prep_2_Free_Licenses__c"]))
            records1.set_value(index, 'Using_Virtual_Servers_Groups__c',
                               str(item["Using_Virtual_Servers_Groups__c"]))
            records1.set_value(index, 'Version__c', str(item["Version__c"]))
            records1.set_value(index, 'of_Dev_Ops_Admin_Ops_Users__c', str(item["of_Dev_Ops_Admin_Ops_Users__c"]))
            records1.set_value(index, 'of_Environments__c', str(item["of_Environments__c"]))
            records1.set_value(index, 'of_Studio_Users__c', str(item["of_Studio_Users__c"]))
            records1.set_value(index, 'of_Testers__c', str(item["of_Testers__c"]))
            records1.set_value(index, 'Usage_Rate__c', str(item["Usage_Rate__c"]))
            records1.set_value(index, 'Customer_Success_SharePoint_Search__c',
                               str(item["Customer_Success_SharePoint_Search__c"]))
            records1.set_value(index, 'personTimeZone', str(item["personTimeZone"]))
            records1.set_value(index, 'Account_Discount__c', str(item["Account_Discount__c"]))
            records1.set_value(index, 'Account_Services_Discount__c', str(item["Account_Services_Discount__c"]))
            records1.set_value(index, 'AVA_SFCPQ__ExemptEntityType__c', str(item["AVA_SFCPQ__ExemptEntityType__c"]))
            records1.set_value(index, 'AVA_SFCPQ__TaxExemptionCode__c', str(item["AVA_SFCPQ__TaxExemptionCode__c"]))
            records1.set_value(index, 'Account_Has_Cust_Terms__c', str(item["Account_Has_Cust_Terms__c"]))
            records1.set_value(index, 'tICDataCenterLocation', str(item["tICDataCenterLocation"]))
            records1.set_value(index, 'tICAcceptTerms', str(item["tICAcceptTerms"]))
            records1.set_value(index, 'dataLakeAccelerator', str(item["dataLakeAccelerator"]))
            records1.set_value(index, 'Remove_Account__c', str(item["Remove_Account__c"]))
            records1.set_value(index, 'Acct_Revenue_MAX__c', str(item["Acct_Revenue_MAX__c"]))
            records1.set_value(index, 'Total_Opps_Stage_2__c', str(item["Total_Opps_Stage_2__c"]))
            records1.set_value(index, 'Partner_Status__c', str(item["Partner_Status__c"]))
            records1.set_value(index, 'Premier_Partner__c', str(item["Premier_Partner__c"]))
            records1.set_value(index, 'Partner_Level__c', str(item["Partner_Level__c"]))
            records1.set_value(index, 'Lead__c', str(item["Lead__c"]))
            records1.set_value(index, 'Account__c', str(item["Account__c"]))
            records1.set_value(index, 'Dietary_Requirements', str(item["Dietary_Requirements"]))
            records1.set_value(index, 'qbdialer__Related_Contact_Dials__c',
                               str(item["qbdialer__Related_Contact_Dials__c"]))
            records1.set_value(index, 'qbdialer__Related_Contact_LastCallTime__c',
                               str(item["qbdialer__Related_Contact_LastCallTime__c"]))
            records1.set_value(index, 'Primary_Partner_Level__c', str(item["Primary_Partner_Level__c"]))
            records1.set_value(index, 'Primary_Partner_Owner__c', str(item["Primary_Partner_Owner__c"]))
            records1.set_value(index, 'Primary_Partner_Type__c', str(item["Primary_Partner_Type__c"]))
            records1.set_value(index, 'Primary_Premier_Partner__c', str(item["Primary_Premier_Partner__c"]))
            records1.set_value(index, 'Sourcing_Partner__c', str(item["Sourcing_Partner__c"]))
            records1.set_value(index, 'MQL_Date_Time_Last__c', str(item["MQL_Date_Time_Last__c"]))
            records1.set_value(index, 'bTLKLevel', str(item["bTLKLevel"]))
            records1.set_value(index, 'bTLKUserID', str(item["bTLKUserID"]))
            records1.set_value(index, 'bTLKLeadContext', str(item["bTLKLeadContext"]))
            records1.set_value(index, 'bTLKLeadType', str(item["bTLKLeadType"]))
            records1.set_value(index, 'bTLKReferral', str(item["bTLKReferral"]))
            records1.set_value(index, 'bTLKChannelID', str(item["bTLKChannelID"]))
            records1.set_value(index, 'bTLKChannelName', str(item["bTLKChannelName"]))
            records1.set_value(index, 'bTLKChannelOrganization', str(item["bTLKChannelOrganization"]))
            records1.set_value(index, 'bTLKChannelsBrightTALKURL', str(item["bTLKChannelsBrightTALKURL"]))
            records1.set_value(index, 'bTLKEngagementScore', str(item["bTLKEngagementScore"]))
            records1.set_value(index, 'bTLKTimeZone', str(item["bTLKTimeZone"]))
            records1.set_value(index, 'bTLKEmbedMarketoToken', str(item["bTLKEmbedMarketoToken"]))
            records1.set_value(index, 'bTLKEmbedURL', str(item["bTLKEmbedURL"]))
            records1.set_value(index, 'bTLKEmbedUTMSource', str(item["bTLKEmbedUTMSource"]))
            records1.set_value(index, 'bTLKEmbedUTMTerm', str(item["bTLKEmbedUTMTerm"]))
            records1.set_value(index, 'bTLKEmbedUTMMedium', str(item["bTLKEmbedUTMMedium"]))
            records1.set_value(index, 'bTLKEmbedUTMContent', str(item["bTLKEmbedUTMContent"]))
            records1.set_value(index, 'bTLKEmbedUTMCampaign', str(item["bTLKEmbedUTMCampaign"]))
            records1.set_value(index, 'bTLKActivityType', str(item["bTLKActivityType"]))
            records1.set_value(index, 'bTLKWebcastID', str(item["bTLKWebcastID"]))
            records1.set_value(index, 'bTLKWebcastURL', str(item["bTLKWebcastURL"]))
            records1.set_value(index, 'bTLKWebcastTitle', str(item["bTLKWebcastTitle"]))
            records1.set_value(index, 'bTLKLastActivityDate', str(item["bTLKLastActivityDate"]))
            records1.set_value(index, 'bTLKLiveMinutesViewed', str(item["bTLKLiveMinutesViewed"]))
            records1.set_value(index, 'bTLKRecordedMinutesViewed', str(item["bTLKRecordedMinutesViewed"]))
            records1.set_value(index, 'bTLKTotalMinutesViewed', str(item["bTLKTotalMinutesViewed"]))
            records1.set_value(index, 'bTLKViewingURL', str(item["bTLKViewingURL"]))
            records1.set_value(index, 'bTLKUTMSource', str(item["bTLKUTMSource"]))
            records1.set_value(index, 'bTLKUTMTerm', str(item["bTLKUTMTerm"]))
            records1.set_value(index, 'bTLKUTMMedium', str(item["bTLKUTMMedium"]))
            records1.set_value(index, 'bTLKUTMContent', str(item["bTLKUTMContent"]))
            records1.set_value(index, 'bTLKUTMCampaign', str(item["bTLKUTMCampaign"]))
            records1.set_value(index, 'bTLKWebcastPresenter', str(item["bTLKWebcastPresenter"]))
            records1.set_value(index, 'bTLKWebcastDuration', str(item["bTLKWebcastDuration"]))
            records1.set_value(index, 'bTLKWebcastDurationMinutes', str(item["bTLKWebcastDurationMinutes"]))
            records1.set_value(index, 'bTLKCreatedDate', str(item["bTLKCreatedDate"]))
            records1.set_value(index, 'bTLKPreregistered', str(item["bTLKPreregistered"]))
            records1.set_value(index, 'bTLKLiveViewingDuration', str(item["bTLKLiveViewingDuration"]))
            records1.set_value(index, 'bTLKLiveViewingsCount', str(item["bTLKLiveViewingsCount"]))
            records1.set_value(index, 'bTLKRecordedViewingDuration', str(item["bTLKRecordedViewingDuration"]))
            records1.set_value(index, 'bTLKRecordedViewingsCount', str(item["bTLKRecordedViewingsCount"]))
            records1.set_value(index, 'bTLKTotalViewingDuration', str(item["bTLKTotalViewingDuration"]))
            records1.set_value(index, 'bTLKTotalViewingsCount', str(item["bTLKTotalViewingsCount"]))
            records1.set_value(index, 'bTLKMarketoToken', str(item["bTLKMarketoToken"]))
            records1.set_value(index, 'bTLKAttachmentID', str(item["bTLKAttachmentID"]))
            records1.set_value(index, 'bTLKAttachmentTitle', str(item["bTLKAttachmentTitle"]))
            records1.set_value(index, 'bTLKAttachmentType', str(item["bTLKAttachmentType"]))
            records1.set_value(index, 'bTLKAttachmentURL', str(item["bTLKAttachmentURL"]))
            records1.set_value(index, 'bTLKFirstAccessedDate', str(item["bTLKFirstAccessedDate"]))
            records1.set_value(index, 'bTLKAttachmentActivityID', str(item["bTLKAttachmentActivityID"]))
            records1.set_value(index, 'bTLKLastAccessedDate', str(item["bTLKLastAccessedDate"]))
            records1.set_value(index, 'bTLKLiveViewAccessCount', str(item["bTLKLiveViewAccessCount"]))
            records1.set_value(index, 'bTLKRecordedAccessCount', str(item["bTLKRecordedAccessCount"]))
            records1.set_value(index, 'bTLKTotalAccessCount', str(item["bTLKTotalAccessCount"]))
            records1.set_value(index, 'bTLKLastAccessURL', str(item["bTLKLastAccessURL"]))
            records1.set_value(index, 'bTLKLastAccessMarketoToken', str(item["bTLKLastAccessMarketoToken"]))
            records1.set_value(index, 'bTLKLastAccessUTMCampaign', str(item["bTLKLastAccessUTMCampaign"]))
            records1.set_value(index, 'bTLKLastAccessUTMContent', str(item["bTLKLastAccessUTMContent"]))
            records1.set_value(index, 'bTLKLastAccessUTMMedium', str(item["bTLKLastAccessUTMMedium"]))
            records1.set_value(index, 'bTLKLastAccessUTMSource', str(item["bTLKLastAccessUTMSource"]))
            records1.set_value(index, 'bTLKLastAccessUTMTerm', str(item["bTLKLastAccessUTMTerm"]))
            records1.set_value(index, 'First_Activity_Time__c', str(item["First_Activity_Time__c"]))
            records1.set_value(index, 'Total_Activities_Including_Outreach_Dia__c',
                               str(item["Total_Activities_Including_Outreach_Dia__c"]))
            records1.set_value(index, 'Total_Activities_MQL_With_Outreach__c',
                               str(item["Total_Activities_MQL_With_Outreach__c"]))
            records1.set_value(index, 'Total_Number_of_Activities__c', str(item["Total_Number_of_Activities__c"]))
            records1.set_value(index, 'Total_Number_of_Activities_since_MQL__c',
                               str(item["Total_Number_of_Activities_since_MQL__c"]))
            records1.set_value(index, 'ddc_prospector__Sourced_from_Data_com__c',
                               str(item["ddc_prospector__Sourced_from_Data_com__c"]))
            records1.set_value(index, 'ddc_prospector__Sourced_from_Data_com__c_account',
                               str(item["ddc_prospector__Sourced_from_Data_com__c_account"]))
            records1.set_value(index, 'ddc_prospector__Sourced_from_Data_com__c_contact',
                               str(item["ddc_prospector__Sourced_from_Data_com__c_contact"]))
            records1.set_value(index, 'Contacts_Previous_Experience__c',
                               str(item["Contacts_Previous_Experience__c"]))
            records1.set_value(index, 'Secondary_Account_Revenue__c', str(item["Secondary_Account_Revenue__c"]))
            records1.set_value(index, 'Secondary_Account_Revenue_Source__c',
                               str(item["Secondary_Account_Revenue_Source__c"]))
            records1.set_value(index, 'Contact_ID_long__c', str(item["Contact_ID_long__c"]))
            records1.set_value(index, 'Resource_URL', str(item["Resource_URL"]))
            records1.set_value(index, 'Resource_Name', str(item["Resource_Name"]))
            records1.set_value(index, 'Resource_ID', str(item["Resource_ID"]))
            records1.set_value(index, 'Account_Segment_CFY__c', str(item["Account_Segment_CFY__c"]))
            records1.set_value(index, 'Is_Domestic_Parent__c', str(item["Is_Domestic_Parent__c"]))
            records1.set_value(index, 'Domestic_Parent__c', str(item["Domestic_Parent__c"]))

        a = a + len(leads)
        print(a)
        if b > 0:
            records1.to_csv(export_file, sep=',', header=True, encoding='utf-8-sig', index=False, mode='a')