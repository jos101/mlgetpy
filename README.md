# mlgetpy
Python Package to extract  data sets from the Center for Machine Learning and Intelligent Systems
https://archive.ics.uci.edu/ml/index.php

# Quick Use
Install the package...

    pip install .

Load repos in dataframe
    
    from mlrgetpy.Repository import Repository
    repo = Repository()
    repo.load()
    df = repo.getData()
    df = df.filter(items=[719, 691, 735, 693,683,696,690,730,613], axis="index")
    print(df) 
