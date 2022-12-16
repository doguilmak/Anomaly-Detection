<h1  align=center><font  size = 6>Anomaly Detection</font></h1>

<p align="center">
    <img src="https://images.pexels.com/photos/1556707/pexels-photo-1556707.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"> 
</p>

<small>Picture Source:<a  href="https://www.pexels.com/tr-tr/@daniel-reche-718241/">Daniel Reche</a></small>

<br>

<h2>Statement</h2>

<p>In this project, I would like to present 4 different anomaly detection algorithms with an example. These  anomaly detection algorithms presented by sklearn. As listed:</p>

<ul>
	<li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor">Local Outlier Factor</a></li>
	<li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope">Elliptic Envelope</a></li>
	<li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM">One Class SVM</a></li>
	<li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html">Isolation Forest</a></li>
</ul>

<br>


<h3>Keywords</h3>
<ul>
	<li>Computer Science</li>
	<li>Anomaly Detection</li>
	<li>Isolation forest</li>
	<li>Local Outlier Factor</li>
	<li>Elliptic Envelope</li>
	<li>One Class SVM</li>
</ul>

<br>

<h3>Dictionary meaning of the word anomaly</h3>

<ol>
	<li>Something different, abnormal, peculiar, or not easily classified : something  anomalous  They regarded the test results as an anomaly.</li>    
	<li>deviation from the common rule : IRREGULARITY.</li> 
	<li>The angular distance of a planet from its as seen from the sun.</li>
</ol>

<br>

<h3>What is Anomaly Detection?</h3>

<p>In data analysis, anomaly detection (also outlier detection) is the identification of rare items, events or observations which raise suspicions by differing significantly from the majority of the data. Typically the anomalous items will translate to some kind of problem such as bank fraud, a structural defect, medical problems or errors in a text. Anomalies are also referred to as outliers, novelties, noise, deviations and exceptions. </p>

<p>Anomaly detection has 3 broad cathegories; <i>Unsupervised anomaly detection</i>,  <i>Supervised anomaly detection</i> and <i>Semi-supervised anomaly detection</i>. We are going to build Unsupervised anomaly detection with <i>Local Outlier Factor</i>, <i>Elliptic Envelope</i>, <i>One Class SVM</i> and <i>Isolation Forest</i>. <p>

<br>

<h3>How to detect Anomalies?</h3>

Simple statistical techniques such as mean, median, quantiles can be used to detect univariate anomalies feature values in the dataset. Various data visualization and exploratory data analysis techniques can be also be used to detect anomalies.

<h2>Dataset</h2>

<p>We will compare their performance with a random sample dataset.</p>

    from sklearn.datasets import make_blobs
    
    n_samples_1 = 1300
	X, y = make_blobs(n_samples=n_samples_1, centers=[[4, 4]], cluster_std=0.45)

<p>As you can see from the code block, we generated <i>1300</i> samples with <i>0.45</i> standart deviaton. We mentioned our cluster center as <i>x=4</i> and <i>y=4</i> on coordinate plane. <p>

<p align="center">
    <img src="make_blob.png"> 
</p>

<br>

<h2>Analysis</h2>

<h3>Local Outlier Factor</h3>

<p>Unsupervised Outlier Detection using the Local Outlier Factor (LOF).

The anomaly score of each sample is called the Local Outlier Factor. It measures the local deviation of the density of a given sample with respect to its neighbors. It is local in that the anomaly score depends on how isolated the object is with respect to the surrounding neighborhood. More precisely, locality is given by k-nearest neighbors, whose distance is used to estimate the local density. By comparing the local density of a sample to the local densities of its neighbors, one can identify samples that have a substantially lower density than their neighbors. These are considered outliers.</p>

<p align="center">
    <img src="https://miro.medium.com/max/700/1*fDR-jZaTpvHjszy5p8Z5Xg.jpeg"> 
</p>


<p align="center">
    <img src="LocalOutlierFactor_score.png"> 
</p>

<p>Figure on the above is shows LOF scores of data points. The data with <i>larger circle of radius</i> could be outlier data.</p>

<br>

<h3>Elliptic Envelope</h3>

<p>Elliptic Envelope is an object for detecting outliers in a Gaussian distributed dataset.</p>

<p align="center">
    <img src="EllipticEnvelope.png"> 
</p>

<br>

<h3>One Class SVM</h3>

<p>Estimate the support of a high-dimensional distribution. The implementation is based on libsvm.</p>

<p align="center">
    <img src="OneClassSVM.png"> 
</p>

<br>

<h3>Isolation Forest</h3>

<p>Isolation forest is an anomaly detection algorithm. It detects anomalies using isolation, rather than modelling the normal points. In 2007, it was initially developed by <i>Fei Tony Liu</i> as one of the original ideas in his PhD study. The significance of this research lies in its deviation from the mainstream philosophy underpinning most existing anomaly detectors at the time, where all the normal instances are profiled before anomalies are identified as instances that do not conform to the distribution of the normal instances. Isolation forest introduces a different method that explicitly isolates anomalies using binary trees, demonstrating a new possibility of a faster anomaly detector that directly targets anomalies without profiling all the normal instances.</p>

<p align="center">
    <img src="IsolationForest.png"> 
</p>

<br>

<h2>Sources</h2>

<ul>
	<li><a href="https://www.merriam-webster.com/dictionary/anomaly">Merriam Webster_</a></li>
	<li><a href="https://en.wikipedia.org/wiki/Anomaly_detection">Anomaly Detection Wikipedia</a></li>
	<li><a href="https://scikit-learn.org/stable/modules/generated/">Scikit-learn</a></li> 
	<li><a href="https://towardsdatascience.com/5-anomaly-detection-algorithms-every-data-scientist-should-know-b36c3605ea16">Towards Data Science</a></li> 
	<li><a href="https://medium.com/mlpoint/local-outlier-factor-a-way-to-detect-outliers-dde335d77e1a">Medium</a></li> 
	<li><a href="https://en.wikipedia.org/wiki/Isolation_forest">Isolation Forest Wikipedia</a></li>
</ul>

<b>If you would like to dive in to anomaly detection, please visit these websites.</b>

<br>    

<h2>Contact Me</h2>

<p>If you have something to say to me please contact me:</p>  

<ul>
	<li>Twitter: <a  href="https://twitter.com/Doguilmak">Doguilmak</a></li>
	<li>Mail address: doguilmak@gmail.com</li>
</ul>
