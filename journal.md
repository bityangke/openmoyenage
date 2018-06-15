# Proposed challenges
Many of these challenges are variants of domain transfer problems. Target domain is always medieval illuminations. Source domain depends on the application.

## Applications

### Large-scale tSNE to explore images first
https://ai.googleblog.com/2018/06/realtime-tsne-visualizations-with.html

### Face, person, horse extraction
With off-the-shelf detectors

### Single photo restyling
**Source domains:** face close-up photo; person photo.

Pipeline can be: a) do mattting b) style transfer c) blend back. This should transfer pose and appearance.

###  Animoji
**Source domain:** face pose and keypoints.

Given a controlled reference target face appearance, this should transfer pose only.

### VJ
**Source domains:** whole body pose; sketch of face / person; colored sketch of the scene

Given controlled appearance, this should allow to animate the avatar.

Extra: detection of multiple person sketches; good person pose parametrization.

# References
1. [Deformable GANs for Pose-based Human Image Generation](https://arxiv.org/abs/1801.00055)
2. [Unsupervised Creation of Parameterized Avatars](https://arxiv.org/abs/1704.05693)
   * [Unsupervised Cross-Domain Image Generation](https://arxiv.org/abs/1611.02200)
3. [Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593)
   * [Generative Visual Manipulation on the Natural Image Manifold](https://arxiv.org/abs/1609.03552)
4. [High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs](https://arxiv.org/abs/1711.11585)
5. [Self-Attention Generative Adversarial Networks](https://arxiv.org/abs/1805.08318)
6. [Visual Attribute Transfer through Deep Image Analogy](https://arxiv.org/abs/1705.01088)
7. [Deep Painterly Harmonization](https://arxiv.org/abs/1804.03189)
8. [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/abs/1804.07723)
9. [QuaterNet: A Quaternion-based Recurrent Model for Human Motion](https://arxiv.org/abs/1805.06485)
10. [Abstract art with ML](https://janhuenermann.com/blog/abstract-art-with-ml)
