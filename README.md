# ![HybridAnalysis](https://s13.postimg.org/mex3nuox3/debug.png) Hybrid Analysis

## Usage

### Hybrid Analysis Scan Result

```python
from hybridanalysis import HybridAnalysis
ha = HybridAnalysis(api_key='xxxxx', api_secret='yyyyy')
ha.scan(sha256='040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f')
```

```javascript
{
    'response_code': 0,
    'response': [
        {
           'environmentId':'100',
           'sha256':'040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f',
           'state':'SUCCESS',
           'error':'Failed to save report to webservice',
           'submitname':'3257422871.js',
           'environmentDescription':'Windows 7 32 bit',
           'size':4714,
           'type':'ASCII text',
           'targeturl':'',
           'md5':'70a2b7c2b2f9c1abe65baae5f34c9f69',
           'sha1':'f5308a8730bb8c4972b4240c8379ed8954e7a45e',
           'threatlevel':2,
           'isurlanalysis':False,
           'analysis_start_time':'2016-06-14 11:35:07',
           'threatscore':100,
           'isinteresting':False,
           'verdict':'malicious',
           'avdetect':'16',
           'vxfamily':'Nemucod.BB1',
           'compromised_hosts':[
              '166.62.109.86',
              '193.23.244.244'
           ],
           'domains':[
              'osogeq.goldvredy.org',
              'zafronrestaurant.com',
              'ojuhjrykij.goldvredy.org'
           ],
           'hosts':[
              '166.62.109.86',
              '193.23.244.244',
              '212.92.97.33'
           ],
           'total_network_connections':3,
           'total_processes':5,
           'total_signatures':53,
           'classification_tags':[

           ]
        }
    ]
}
```

### Hybrid Analysis Feed
```python
print(ha.feed(days=1)['count'])
```

```javascript
204
```

```python
print(ha.feed(days=1)['data'][0])
```

```javascript
{
   'md5':'ce3291be2ded8b82fc973e5f5473b1fe',
   'sha1':'fcf4cab3ade392c611c95e16c913fbc967577222',
   'sha256':'dd25c99eff8da336213129726862076fad04612478b24e262f9a8684e350e880',
   'isinteresting':False,
   'analysis_start_time':'2018-01-15 21:46:36',
   'threatscore':100,
   'threatlevel':2,
   'threatlevel_human':'malicious',
   'avdetect':72,
   'isunknown':False,
   'vxfamily':'Trojan.Small',
   'submitname':'dd25c99eff8da336213129726862076fad04612478b24e262f9a8684e350e880',
   'isurlanalysis':False,
   'size':6792,
   'type':'PE32 executable (GUI) Intel 80386, for MS Windows, ...',
   'environmentId':'100',
   'environmentDescription':'Windows 7 32 bit',
   'sharedanalysis':True,
   'isreliable':True,
   'reporturl':'/sample/dd25c99eff8da336213129726862076fad04612478b24e262f9a8684e350e880/?environmentId=100',
   'vt_detect':78,
   'ms_detect':72,
   'process_list':[
      {
         'uid':'00040691-00002896',
         'name':'dd25c99eff8da336213129726862076fad04612478b24e262f9a8684e350e880.exe',
         'normalizedpath':'C:\\dd25c99eff8da336213129726862076fad04612478b24e262f9a8684e350e880.exe',
         'commandline':'',
         'sha256':'dd25c99eff8da336213129726862076fad04612478b24e262f9a8684e350e880',
         'av_label':'Trojan.Small',
         'av_matched':34,
         'av_total':47
      }
   ],
   'extracted_files':[

   ]
}
```