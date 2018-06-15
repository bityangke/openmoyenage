# Proposed challenges
Many of these challenges are variants of domain transfer problems. Target domain is always medieval illuminations. Source domain depends on the application.

## Applications
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
4. [Self-Attention Generative Adversarial Networks](https://arxiv.org/abs/1805.08318)
5. [High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs](https://arxiv.org/abs/1711.11585)
6. [Visual Attribute Transfer through Deep Image Analogy](https://arxiv.org/abs/1705.01088)
7. [QuaterNet: A Quaternion-based Recurrent Model for Human Motion](https://arxiv.org/abs/1805.06485)
8. [Abstract art with ML](https://janhuenermann.com/blog/abstract-art-with-ml)
9. [Deep Painterly Harmonization](https://arxiv.org/abs/1804.03189)
