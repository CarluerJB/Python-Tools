# Python-Tools
Some Python Tools for all kind of Analysis

## 3D SIFT Tools

### 3D_SIFT_match_comparator
#### Description
This tool allow to compare the output of featMatchMultiple. This work like the diff bash command's. 

Statistical information about intersection key-points, and isolated key-points is given.

#### Usage
This script is design to compare file from featMatchMultiple. 
The format accepted is .key.matches.img. But no check is made over here.

    python 3D_SIFT_match_comparator.py [options] <File 1> <File 2>
  
		<File 1,2>: text file containing matches coordinates
		[options]
		  -v         : (verbose) output information about coordinates for each modality.

***
### splitFeature
#### Description
This tool allow to split the output of featExtract according to origin of key-points.

Key-points are split in peaks or valleys.

#### Usage
This script is design to split file from featExtract. 
The format accepted is .key But no check is made over here.
Output is set to the directory peak and the directory valley.

Be carefull ! These directory are deleted before any operation

    python splitFeature.py [options] <Input 1>
  
		<Input 1>: List of .key files, or filename containing this list
		[options]
		  -f         : (file) If Input 1 is a text file containing a list of key-point files location.
***
