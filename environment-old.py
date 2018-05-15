#!/usr/bin/python
def getenv(environment):
	if environment == 'HLO_TEST':
		env = [
			{"HOST":"10.2.0.195","PROJECT":"zn_ihlocs05_vhlocs00","LUN":"zn_ihlocs05_vhlocs00","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
    		{"HOST":"10.2.0.195","PROJECT":"fs_vhlocs03_backup","LUN":"backup","POOL":"VM-MIRROR","enabled":"false","continuous":"false"},
  	  		{"HOST":"10.2.0.195","PROJECT":"db_vhlocs03_hloarch","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
   	 		{"HOST":"10.2.0.195","PROJECT":"db_vhlocs03_hlocont","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_vhlocs03_hloprod","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_vhlocs03_hlosalsa","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_vhlocs04_gullprod","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"fs_vhlocs02_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_vhlocs04_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"ld_ihlocs02_vhlocs01","LUN":"ldompool-vhlocs01","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_vhlocs01_vhlocs02","LUN":"rpool","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_vhlocs01_vhlocs03","LUN":"rpool","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_vhlocs01_vhlocs04","LUN":"rpool","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.191","PROJECT":"zn_vhlocs22_vhlocs20","LUN":"rpool","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.191","PROJECT":"fs_vhlocs03_backup","LUN":"backup","POOL":"VM-MIRROR","enabled":"false","continuous":"false"}]

	if environment == 'FCL_TEST':
		env = [
			{"HOST":"10.2.0.195","PROJECT":"db_aclys03_fcdata","LUN":"database","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},	
    		{"HOST":"10.2.0.195","PROJECT":"db_aclys03_fctest","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
  	  		{"HOST":"10.2.0.195","PROJECT":"fs_aclys03_avail_cache","LUN":"avail-server-cache0","POOL":"VM-MIRROR","enabled":"false","continuous":"false"},
   	 		{"HOST":"10.2.0.195","PROJECT":"db_aclys06_fccont2","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_aclys01_calypso","LUN":"calypso1","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys10_fcrepla","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys02_fcarch","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys06_fctest2b","LUN":"database1","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys06_fctest2","LUN":"database1","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys07_fcreplt2a","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys05_fcreplta","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys03_fccont","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_aclys04_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys04_fctrain","LUN":"database0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys04_fctrain_b","LUN":"database1","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys02_fcprod_b","LUN":"database1","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys03_fctest_b","LUN":"database1","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"db_aclys02_fcarch_b","LUN":"database1","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.191","PROJECT":"fs_aclys03-avail_cache","LUN":"avail-server-cache0","POOL":"VM-MIRROR","enabled":"false","continuous":"false"},
			{"HOST":"10.2.0.191","PROJECT":"fs_iclys00_osb","LUN":"osb","POOL":"VM-MIRROR","enabled":"false","continuous":"false"},
			{"HOST":"10.2.0.191","PROJECT":"fs_iclys01_aclys09","LUN":"servicepool","POOL":"VM-MIRROR","enabled":"false","continuous":"false"},
			{"HOST":"10.2.0.191","PROJECT":"zn_iclys00_aclys09","LUN":"rpool","POOL":"VM-MIRROR","enabled":"false","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_aclys07_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_aclys03_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_iclys07_aclys03","LUN":"zoneroot0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_iclys06_aclys08","LUN":"zoneroot0","POOL":"VM-MIRROR","enabled":"true","continuous":"true"},
			{"HOST":"10.2.0.195","PROJECT":"fs_aclys06_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_iclys06_osb","LUN":"osb","POOL":"VM-MIRROR","enabled":"fasle","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_iclys07_aclys04","LUN":"zoneroot0","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"fs_aclys05_calypso","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"},
			{"HOST":"10.2.0.195","PROJECT":"zn_iclys07_aclys07","LUN":"calypso","POOL":"VM-MIRROR","enabled":"true","continuous":"false"}]
	
	return env