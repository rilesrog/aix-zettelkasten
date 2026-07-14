---
title: "Feature Visualization within an Automated Design Assessment leveraging Explainable Artificial Intelligence Methods"
source_url: "http://arxiv.org/pdf/2201.12107v1"
doi: ""
ingest_date: "2026-07-14"
status: "publish"
---

## 31th CIRP Design 2021 (CIRP Design 2021)

# Feature Visualization within an Automated Design Assessment leveraging Explainable Artificial Intelligence Methods

a a a a
Raoul Schönhof*, Artem Werner, J<sup>a</sup>nnes Elstner, Boldizsar Zopcsak

## Ramez Awad a , Marco Huber a

## a a Ramez Awad, Marco Huber

<sup>a</sup>
*Fraunhofer Institute for Manufacturing Engineering and Automation IPA, Nobelstraße 12, Stuttgart, Germany*

* Corresponding author. Tel.: +49-711-970-1843; *E-mail address:* raoul.schoenhof@ipa.fraunhofer.de

Not only automation of manufacturing processes but also automation of automation procedures itself become increasingly relevant to automation 
research. In this context, automated capability assessment, mainly leveraged by deep learning systems driven from 3D CAD data, have been 
presented. Current assessment systems may be able to assess CAD data with regards to abstract features, e.g. the ability to automatically separate 
components from bulk goods, or the presence of gripping surfaces. Nevertheless, they suffer from the factor of black box systems, where an 
assessment can be learned and generated easily, but without any geometrical indicator about the reasons of the system’s decision. By utilizing 
explainable AI (xAI) methods, we attempt to open up the black box. Explainable AI methods have been used in order to assess whether a neural 
network has successfully learned a given task or to analyze which features of an input might lead to an adversarial attack. These methods aim to 
derive additional insights into a neural network, by analyzing patterns from a given input  and its impact to the network’s output. Within the 
NeuroCAD Project, xAI methods are used to identify geometrical features which are associated with a certain abstract feature. Within this work, 
a sensitivity analysis (SA), the layer-wise relevance propagation (LRP), the Gradient-weighted Class Activation Mapping  (Grad-CAM) method 
as well as the Local Interpretable Model-Agnostic Explanations (LIME) have been implemented in the NeuroCAD environment, allowing 
not only to assess CAD models but also to identify features which have been relevant for the network’s decision. In the medium run, this might 
enable to identify regions of interest supporting product designers to optimize their models with regards to assembly processes.

© 2021 The Authors. Published by Elsevier B.V.
Peer-review under responsibility of the scientific committee of the CIRP Design Conference.

## Abstract

Around 70% of the manufacturing costs of a product are 
already defined during the design phase [1].
However, product developers focus their considerations

to features that are difficult to formalize. Accordingly,
automation usually takes place much later in the design
process or not at all. For this reason, automatically deriving
abstract features such as ease of sorting,  feeding and
assembling, which make up considerable cost differences in
For example, minor component adjustments can enable the

However, product developers focus their considerations 
on the implementation of functional features. CAD systems 
typically provide tools to aid in functional and performance 
analysis of the design [2].

*Keywords:* Assembly Automation, Deep Learning, xAI, , NeuroCAD, Grad-CAM, LIME, LRP

Questions about further processing, on the other hand,

1. Introduction use of bowl feeders (~ 5 t €) instead of requiring a complex 
bin  picking  robot  system  with  image  recognition  for 
component separation in extreme cases (~ 200 t €). Similar 
examples can be given for positioning and joining. 
Even though abstract features can be learned from 3D

$$
R_{i}
$$

Even though abstract features can be learned from 3D 
CAD data by neural networks, an inherent problem remains. 
Relevant features are hidden within the network. This lack of 
feedback and interpretability prevents product optimizations.
In this paper we present a toolset comprised of the xAI

(1)

In this paper we present a toolset comprised of the xAI 
Methods sensitivity analysis (SA) [3], the layer-wise 
relevance propagation (LRP) [4], the Gradient-weighted 
Class Activation Mapping (Grad-CAM) method [5] as well 
as the Local Interpretable Model-Agnostic Explanations 
(LIME) [6] for  interpreting  abstract three-dimensional 
features from CAD  models previously learned in neural 
networks by supervised learning approaches. It is structured 
as followed. Chapter 2 depicts a brief overview  of the 
previously  mentioned  xAI  methods  and  their  working 
principals. Chapter 3 then, shows how to adapt them to 
analyse 3D models. Chapter 4 evaluates the adapted methods 
briefly. The paper is completed by a short summary and 
future given in chapter 5 and 6.

## 2. State of the Art Explainable Artificial Intelligence Methods

Within this chapter, we aim to present a brief overview of 
the  most  relevant  methods  of  xAI  and  their  working 
principles in the domain of neural networks.

(2)

## 2.1. Sensitivity Analysis

Sensitivity Analysis aims to determine how a neural 
network’s output is impacted by the input. It is a numeric 
approach to quantify the influence of every input neuron on 
the output  [7][8]. The technique dates back to the 1960s, 
when the link between misclassification and weight/input 
perturbation of self-learning systems was first investigated 
[9].  Given a neural network with known weight,  bias 
variables and architecture, one can propagate the gradient of 
the output layer through differentiation back through each 
individual neuron in the layers prior. This is calculated with 
respect to a loss function, which is generally set to maximize 
the output of a classification neuron [10]. Reaching the input 
layer, the gradient corresponding to the value of each input
neuron can be interpreted as marking the influence of that 
feature.  Gradient  values  near  zero  correspond  to  little 
influence  on  the  output,  whereas  large  ones  highlight 
important features as given in Figure 1.

For the formal definition, the relevance or importance 𝑅<sub>𝑖</sub>
of an input 𝑥 is defined as [10].

$$
R_{i}(x)=\left(\frac{\partial f}{\partial x_{i}}\right)^{2}
$$

The function 𝑓(𝑥) is chosen to be evidence for the true 
class. Decomposing of the gradient square norm yields [10]:

$$
f(x)
$$

$$
{\sum}_{i=1}^{d}R_{i}(x)=\|\nabla f(x)\|^{2}
$$

Sensitivity analysis can also be used to iteratively change 
an input's classification, e.g. with image classification. Once 
the gradients of the input layer have been determined, the 
additional Deep Dream algorithm [3] can be used to modify 
the pixel values corresponding to the gradient. The gradient 
is multiplied by a scaling factor and added onto the image, 
effectively increasing or decreasing pixel values. This output 
is fed back into the network to compound the modification, 
hence the iterative nature.

However, the limitation of sensitivity analysis is that it 
does not provide an explanation for the network’s 
classification, but rather its gradient slope with respect to the 
input values [11]. Thus, the generated heatmap indicates 
pixels that make the object more or less like the target class. 
No interpretable information on what makes the object 
belong to the class is obtained.

## 2.2. Layer-Wise Relevance Propagation

During Layer-wise Relevance Propagation [12] the output 
of the neural network is assigned a relevancy which is 
propagated backward in the network. 
Defining  𝑧 = 𝑎 𝑤 as  the  weighted  activation  of

Defining  𝑧<sub>𝑗𝑘</sub>= 𝑎<sub>𝑗</sub>𝑤<sub>𝑗𝑘</sub>as  the  weighted  activation  of 
neuron  j  onto  neuron  k  in  the  subsequent  layer,  the 
relevancies of the neurons in each layer can be redistributed 
to each neuron j in the preceding layer following the standard 
LRP rule:

(3)

$$
z_{j k}=a_{j}w_{j k}
$$

$$
R _ {j} ^ {(l)} = \sum_ {k} \left(\frac {z _ {j k}}{\sum_ {j} z _ {j k}} R _ {k} ^ {(l + 1)}\right)
$$

In words, neuron j is assigned the share of the relevancy 
of a neuron k in the subsequent layer corresponding to 
neuron j’s contribution to the activation of neuron k. 
To enhance numerical stability, one arrives at the LRP-𝜖

For layers such as convolutional layers where each input 
neuron is not directly connected to each output neuron via a 
weight 𝑤<sub>𝑗𝑘</sub>, the weight has to be interpreted as the gradient
<u>𝜕𝑎𝑘</u>
.
𝜕𝑎𝑗

$$
R _ {j} ^ {(l)} = \sum_ {k} \left(\frac {z _ {j k}}{\sum_ {j} z _ {j k} + \epsilon s i g n (\sum_ {j} z _ {j k})} R _ {k} ^ {(l + 1)}\right)
$$

To enhance numerical stability, one arrives at the LRP-𝜖
rule by adding a small term 𝜖 in the denominator.

The propagation is implemented in four steps (see [4]).

$$
\frac{\partial a_{k}}{\partial a_{j}}
$$

Figure 1: A CNN-Classifier trained on the MNIST dataset is used to

---

(5)
(6)

$$
\ z\==\varepsilon+l a y e r(a)\;\;\;\ \S{!e p p},\,
$$

(6)
(7)

$$
c = \nabla \langle z, [ s ] _ {c s t} \rangle \quad S t e p 3
$$

(7)
(8)

$$
R ^ {(l)} = a \odot c \quad S t e p 4
$$

(8)

Figure  2 shows an example of how to achieve this by a 
Tensorflow 2 implementation.

[Image: Image75]

[Image: Image75]
Figure 2: Example of the relevancy redistribution between two layers of 
the neural network.

Applying this rule iteratively starting from the output 
layer until reaching the input layer, one ends up with 
relevancies assigned to the voxels which attempt to model 
their  individual  importance  to  the  network  classifier’s 
decision.

There also exists an alternative framework by which to 
compute LRP for a wider array of network architectures, 
which is described in [13].
Useful out-of-the-box LRP implementations are

Useful out-of-the-box LRP implementations are
DeepExplain [4] or iNNvestigate [14].

LRP  has many  desirable  properties  and  results  in 
heatmaps of high quality than most other methods [15].
The first among these qualities is that LRP fulfils the

heatmaps of high quality than most other methods [15].
The first among these qualities is that LRP fulfils the 
conversation principle, meaning that no relevancy is lost 
during the propagation.

$$
\sum_{j}\left(\,R_{j}^{\;(l+1)}\right)\,=\,\sum_{k}\left(\,R_{k}^{\;(l+1)}\right)
$$

𝑗 𝑘
Additionally, LRP heatmaps visualize features which are 
relevant for the network’s decision, not which changes in 
features  affect  the  network  the  most,  like  Sensitivity 
Analysis. The results obtained by LRP are also stable in the 
sense that small changes in the input do not significantly 
change the heatmaps assuming the network’s decision was 
not altered significantly either. Lastly, LRP allow for the 
interpretation of both positive and negative evidence 
supporting/undermining the classifier’s prediction.

## 2.3. LIME

and measures the distance of the resulting predictions to the 
prediction of the original input data. This distance is mapped 
to a value between zero and one called weight which 
represent similarity between the original input data and the 
perturbed data. Thereby, the zero represent maximal 
dissimilarity and the one represents maximal similarity.

Finally, a statistical method is applied on weights to 
explain the prediction of the classifier. Thus, there is a higher 
probability to approximate the amount of top features in the 
input data used by a classifier to make a certain decision. 
Because this algorithm is an optimization-based method that 
requires multiple iterations through a classifier, it is time and 
resource consuming. Ribeiro et al. describes another
approach to explain the prediction of a single image on the 
Inception network. The first advantage of the algorithm is the 
classifier’s independence which offers the flexibility and 
future-proof  work  with  the  next  generation  classifiers. 
Another advantage is the simple interpretability of the 
explanation. When a region of the input data is highlighted 
in the output, then it means that this region is important for 
the decision of the classifier [16].

Formally, the LIME algorithm is defined by:

$$
\zeta(x)=a r g m i n\mathcal{L}(f,g,\pi_{x})+\mathcal{I}(g)
$$

where 𝑥 is the input data being explained, 𝑔 is a statistical 
method and 𝛺(𝑔) is the complexity of this statistical method. 
The locality-aware loss function 𝓛(𝑓, 𝑔, 𝜋<sub>𝑥</sub>) is defined by:

$$
\mathcal{L}(f,g,\pi_{x})
$$

$$
\mathcal{L}(f,g,\pi_{x})={\textstyle\sum}\pi_{x}(z)(f(z)-g(z^{\prime}))^{2}
$$

The proximity  𝜋<sub>𝑥</sub>between the original input and 
perturbed data 𝑧 is defined by:

$$
\pi_ {x} (z) = \exp \left(- D (x, z) ^ {2} / \sigma^ {2}\right)
$$

where exp is the exponential kernel,  𝐷 is the distance 
metric and 𝜎 is the width. The width defines the locality 
around the data.

The class activation mapping (CAM) method explains the 
prediction of a neural network by visualizing a heat map to 
the user. The idea behind the algorithm is that each activation 
map in the convolution layer preceding the GAP layer detects 
a different pattern in the input data. To get the heat map, the 
algorithm computes the sum of each recognized pattern in 
the activation maps. A recognized pattern, which belongs to 
the target class, has a greater impact  on the sum. This is 
possible because each node in the GAP layer represents a 
different activation map and the weights between the GAP 
layer and the dense layer maps each activation map’s 
contribution to the target class. An advantage of this method 
is that it requires only one iteration through the classifier [16]. 
This iteration consists of one forward and one backward pass 
which has a positive impact on computing resources and is 
in contrast to the perturbation-based method. One of the 
disadvantages of this method is the lack of  interpretability 
[16] of the result. A description should be provided, enabling 
the user  to get an  understandable explanation. Another

pixel mask is computed by using a segmentation algorithm.
grayed out super-pixels of the mask to the input data. A a

## 2.4. Grad-CAM

---

disadvantage is that the penultimate convolution layer should 
be an average pooling layer (GAP) [16].

The Grad-CAM  [5] algorithm bypasses this problem by 
back-propagating the gradients of  the  last fully connected 
layer to the last convolutional layer, to produce  a  coarse
localization map of important regions in the input data. The 
convolutional layers contain semantic and spatial 
information of the input data which is lost in the fully 
connected layers.  The  Grad-CAM algorithm passes the 
gradients of the prediction to the last convolutional 
producing a localization map. This localization map contains 
spatial information of important regions which are coarsely 
highlighted. The important regions for a particular layer k are 
defined by:

(13)

$$
\alpha_{k}^{c}=\frac{1}{Z}\ {sum{\sum}_{i}}{{\sum}_{j}}\frac{{\partial{y^{c}}}}{{\partial{A_{i j}^{k}}}}
$$

where

(14)

$$
Z=\sum_{i}\sum_{j}1
$$

𝑖 𝑗
𝑐
is the number of pixels in the feature map,  𝜕𝑦 is the 
𝑘
gradient of the score for the class 𝑐 and 𝜕𝐴<sub>𝑖𝑗</sub>is the gradient 
𝑘
of feature activations 𝐴 of the convolutional layer. Finally,
the localization map is defined by:

$$
\partial y^{c}
$$

$$
\partial A_{i j}^{k}
$$

$$
A^{k}
$$

(15)

$$
L^{c}=R e L U(\sum_{k}\alpha_{k}^{c}A^{k})
$$

where 𝑅𝑒𝐿𝑈is a rectified linear unit function. The result 
is a heat map with the same dimension as the convolutional 
layer 𝑘 . It has to be mentioned, that  Grad-CAM had been
applied to  3D input and is used to assess production costs 
with 3D parts [17].

3. Proposed Work

Within this chapter, we present a range of adaptions for 
the previously described  xAI methods as far as they are 
necessary.  This establishes a toolbox for interpreting 3D
CAD features learned by  neural  networks. Within the 
following chapters, the xAI methods have been applied to the 
NeuroCAD networks [18] by analysing the same sheet metal 
part shown in Figure 3.

## 3.1. Sensitivity Analysis 3D

component. Figure 4 shows the output of the networks for a 
motor sheet.

[Image: Image85]
Figure 4: One can observe the plot of each of the 11 output neurons plotted 
against their activation. A spike in the lower, middle and upper 
neurons indicates a low, average and high degree of the respective 
assessment, in this case grabability.

To propagate the gradients back through the network, a 
loss function is defined to maximise the largest activation of 
the 11  output neurons.  Figure  5 shows the heatmap of the
network, showing regions of positive and negative influence 
to the network’s classification, whereas more yellow regions 
are associated with a higher influence and transparent 
regions are associated with a lower influence.

[Image: Image88]
Figure 6: more intense the The corresponding LRP heatmap of the sheet metal part. The 
colour, the stronger the supporting evidence of 
the classifier’s decision.

[Image: Image87]
Figure 5: Heatmap for the sheet metal part, which was assessed for the 
abstract feature “grabability”.

## 3.2. Layer-Wise Relevance Propagation 3D

When handling 3D models, Layer-wise Relevance 
Propagation comes very handy. It works for both 2D inputs 
(e.g.  images)  and  for  the  3D  voxel  models  used  for 
NeuroCAD without any modification to the algorithm.

---

## 3.3. LIME 3D

We  applied the  LIME algorithm on 3D  CAD data 
represented by point clouds to  derive explanations of the 
classifier’s predictions. In case of monotonous point clouds,
we cannot use a heterogeneous segmentation algorithm, as 
they partition the data on different colorspace  criteria.  A 
homogeneous segmentation algorithm is also not an option,
because the segmentation results in granular segments [5]. 
The perturbed data was created by  applying the uniform 
three-dimensional grid to the input data as seen in Figure 6. 
This approach allows us to control the amount and the size 
of segments used to split the data which are similar to the 
super-pixels approach described by Ribeiro et al.  and also 
does not require lots of computing resources. The output was 
predicted with a neural network and each prediction was 
converted to weights as described above. We use a cosine 
metric as a distance function to measure the proximity 
between the prediction of the original input data and each 
randomly generated perturbation. The distances were 
converted to weights by an exponential kernel function 
proposed by Ribeiro et al. The linear regression was used as 
the statistical method to generate important coefficients. 
Each coefficient represents one segment in the perturbed data. 
These coefficients were used to produce the amount of top 
features which are important for the decision of the neural 
network.  These  top  features  represents  the  classifier’s
prediction which is shown in Figure 7.

[Image: Image98]
Figure 7: The uniform three-dimensional grid with 3D CAD point cloud.

## 3.4. Grad-CAM 3D

At first, we passed the input data through the classifier and 
grabbed the neuron activation of a given prediction. At the 
most, this is the top predicted class.  Using Tensorflow's 
automatic differentiation, the gradient of the score by use of 
automatic differentiation with respect to the output feature 
map of the last convolutional layer was computed. Then, the 
gradients are multiplied with the activation of the feature 
map with respect to the predicted class. Finally, the resulting 
heat map is normalized and scaled to the dimension of the 
input data. To create a superimposed visualization, we 
normalize the input data and multiply it with the resulting 
heat map. The output is the voxel model representing a 3D 
CAD data which visualize regions that are important for the 
prediction with higher byte values and regions that are 
irrelevant with lower byte values.  This output is shown in 
Figure 8 by applying a colour map in order to improve the 
interpretability for a user.
[Image: Image100]

[Image: Image100]
Figure 8: The result of Grad-CAM algorithm. The yellow or orange colour 
space represents the relevant regions. The blue colour space 
represents irrelevant regions.

For evaluation, a simple 3D CNN was created. This was 
done by first pretraining an autoencoder unsupervised. Then,
a  supervised  transfer  learning  with  labelled data  was 
performed.

The current NeuroCAD trainset for abstract 
manufacturing features is quite small (approx. 200 models)
[18], which is why only relying on model augmentation can 
lead to an overfitting. To overcome this issue, a large part of 
the network was  pretrained by using an autoencoder. This 
allowed to use unsupervised learning approaches and large, 
already existing, trainsets. For pretraining, the autoencoder 
was trained by 10.000 models from the ABC trainset [20].

separability, grabability and orientability. These values have
associated fitness from an  automation  expert’s perspective

---

## 4.3. Results

An overview of the different xAI method outputs is 
depicted in Table 1.

| Method | Grabability | Seperabitily | Orientability |
| --- | --- | --- | --- |
| LIME/Jet |  |  |  |
| Grad-CAM |  |  |  |
| Sensitivity Analysis |  |  |  |
| LRP |  |  |  |

other 3D model representation. Especially the investigation 
of point cloud models could lead to the direct assessment of 
scanned models, leveraging 3D assessments of physical 
parts.

## 5. Conclusion

## 7. Acknowledgements

CAM 3D, SA 3D and LRP 3D. The networks analysed had been taken from
the NeuroCAD project [18].

**References**
[1] Boothroyd, G. 1994. “Product design for manufacture and 
assembly”. Computer-Aided Design, 26(7): 505-520.
[2] Locascio, A. Manufacturing Cost Modeling for Product Design. 
International Journal of Flexible Manufacturing Systems 12, 207–217 
(2000). https://doi.org/10.1023/A:1008199714982.
[3] Alexander M., Christopher O., Mike T., Inceptionism: Going Deeper 
into Neural Networks, Google AI Blog, 17.06.2015.
[4] Samek, W., Montavon, G., Lapuschkin, S., Anders, C. J., and Müller, 
K.-R., Toward interpretable machine learning: Transparent deep 
neural networks and beyond, CoRR, 2020.
[5] Jagadish H., Prakash J., A Novel Method for Homogeneous Region 
Based Image Segmentation Technique for Remotely Sensed Images, 
2015.
[6] M.T. Ribeiro, S. Singh, C. Guestrin, ArXiv:1602.04938 [Cs, Stat], 
2016.
[7] Oh S. and Lee Y., Sensitivity analysis of single hidden-layer neural 
networks with threshold functions, in IEEE Transactions on Neural 
Networks, vol. 6, no. 4, pp. 1005-1007, July 1995, doi: 
10.1109/72.392264.
[8] Choi J. and Choi C., Sensitivity analysis of multilayer perceptron with 
differentiable activation functions, in IEEE Transactions on Neural 
Networks, vol. 3, no. 1, pp. 101-107, Jan. 1992, doi: 
10.1109/72.105422.
[9] Widrow B., Lehr M., Artificial neural networks of the perceptron, 
madaline, and backpropagation family, Neurobionics, Elsevier, 1993, 
pp. 133-205, ISBN: 9780444899583.
[10] Montavon G., Samek W., Müller K.-R., Methods for interpreting and 
understanding  deep  neural  networks, Digital  Signal  Processing,
Volume 73, 2018, Pages 1-15, ISSN 1051-2004.
[11] Wojciech  S., Grégoire  M., Sebastian  L., Christopher J. Anders, and 
Klaus-Robert Müller, Toward Interpretable Machine Learning: 
Transparent Deep Neural Networks and Beyond, 2020,
arXiv:2003.07631.
[12] Bach S,  Binder A,  Montavon G,  Klauschen F,  Müller KR,  et  al. 
(2015) On Pixel-Wise Explanations for Non-Linear Classifier 
Decisions by Layer-Wise Relevance Propagation. PLOS ONE 10(7): 
e0130140
[13] Ancona M., Ceolini E., Öztireli, C. and Gross M.. Towards better 
understanding of gradient-based attribution methods for deep neural 
networks. arXiv preprint arXiv:1711.06104, 2017.
[14] Alber, M., Lapuschkin, S., Seegerer, P., Hägele, M., Schütt, K. T., 
Montavon, G., Samek, W., Müller, K. R., Dähne, S., & Kindermans, 
P. J. (2019). iNNvestigate neural networks! J. of Machine Learning 
Research, 20.
[15] Samek W., Binder A., Montavon G., Bach S., and Müller K.-R.. 2015. 
Evaluating the visualization of what a Deep Neural Network has 
learned. CoRR, 2015, arXiv:1509.06321.
[16] R. Fong, A. Vedaldi, in: W. Samek, G. Montavon, A. Vedaldi, L.K. 
Hansen, K.-R. Müller (Eds.), Explainable AI: Interpreting, Explaining 
and Visualizing Deep Learning, Springer International Publishing, 
Cham, 2019, pp. 149–167.
[17] Yoo, S., Kang, N., Explainable Artificial Intelligence for 
Manufacturing Cost Estimation and Machining Feature Visualization, 
IJCSIT, Vol. 6, 2020..
[18] Schönhof R., Fechter M., Towards automated Capability Assessment 
leveraging Deep Learning, Procedia CIRP, Vol. 91, 2020, pp. 433-
438.
[19] R.R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, D. 
Batra, Int J Comput Vis 128 (2020) 336–359.
[20] Koch, S., Matveev, A., Jiang, Z., Williams, F., Artemov, A., Burnaev, 
E., Alexa, M., Zorin, D., Panozzo, D., ABC: A Big CAD Model 
Dataset For Geometric Deep Learning, in: IEEE CVPR, June 2019.

Within this work, a toolbox of the most current xAI 
Methods have been presented, which have been adapted to 
support 3D inputs.  Thus enabling the users to analyse neural 
network  based  decisions  made  on  3D  voxel  models.
Comparable to 2D image analysis, these tools will allow the 
interpretation  of  complex-abstract  features  assessed  by 
neural networks.

As already stated, the 3D xAI methods, only allow to
highlight regions of  the  CAD part which are  especially
interpretation. Therefore the next task, will be to create a
metrology how to interpret the generated results.  Being able

designers in order to improve  their designs.  Also the
## presented toolbox was tailored for  handling voxel models.

The  research  presented  in  this  paper  has  received  
partial funding by the  AI-Innovation Centre “Learning  
Systems” (KI-FZ)  (10/2019 - 03/2021).

## References [1] Boothroyd, G. 1994. “Product design for manufacture and