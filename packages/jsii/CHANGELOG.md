# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

<a name="0.7.11"></a>
## [0.7.11](https://github.com/awslabs/jsii/compare/v0.7.10...v0.7.11) (2018-11-18)




**Note:** Version bump only for package jsii

<a name="0.7.10"></a>
## [0.7.10](https://github.com/awslabs/jsii/compare/v0.7.9...v0.7.10) (2018-11-12)


### Bug Fixes

* **jsii:** jsii-fix-peers missing in npm tarball ([#313](https://github.com/awslabs/jsii/issues/313)) ([6915455](https://github.com/awslabs/jsii/commit/6915455))




<a name="0.7.9"></a>
## [0.7.9](https://github.com/awslabs/jsii/compare/v0.7.8...v0.7.9) (2018-11-12)


### Bug Fixes

* **docs:** improve docs rendering ([#303](https://github.com/awslabs/jsii/issues/303)) ([094a215](https://github.com/awslabs/jsii/commit/094a215)), closes [#301](https://github.com/awslabs/jsii/issues/301) [#298](https://github.com/awslabs/jsii/issues/298) [#302](https://github.com/awslabs/jsii/issues/302) [#300](https://github.com/awslabs/jsii/issues/300) [#299](https://github.com/awslabs/jsii/issues/299)
* **jsii:** do not mark "any" or "unknown" as optional (unless "?") ([#295](https://github.com/awslabs/jsii/issues/295)) ([cdf5a53](https://github.com/awslabs/jsii/commit/cdf5a53)), closes [#284](https://github.com/awslabs/jsii/issues/284)
* **runtime/dotnet:** Correct a number of type mappings ([#291](https://github.com/awslabs/jsii/issues/291)) ([0d59dab](https://github.com/awslabs/jsii/commit/0d59dab)), closes [#290](https://github.com/awslabs/jsii/issues/290) [awslabs/aws-cdk#1027](https://github.com/awslabs/aws-cdk/issues/1027)
* accept variadic arguments after optional arguments ([#307](https://github.com/awslabs/jsii/issues/307)) ([c1af1d6](https://github.com/awslabs/jsii/commit/c1af1d6))
* remove overly strict checks on peer versions ([#306](https://github.com/awslabs/jsii/issues/306)) ([7b89d01](https://github.com/awslabs/jsii/commit/7b89d01))


### Features

* **jsii:** enforce peer dependencies ([#294](https://github.com/awslabs/jsii/issues/294)) ([1753910](https://github.com/awslabs/jsii/commit/1753910)), closes [awslabs/aws-cdk#979](https://github.com/awslabs/aws-cdk/issues/979)




<a name="0.7.8"></a>
## [0.7.8](https://github.com/awslabs/jsii/compare/v0.7.7...v0.7.8) (2018-10-23)


### Bug Fixes

* **jsii:** use base interfaces for 'datatype' property ([#265](https://github.com/awslabs/jsii/issues/265)) ([1c56902](https://github.com/awslabs/jsii/commit/1c56902)), closes [#264](https://github.com/awslabs/jsii/issues/264)
* match behavioral interface to 'I'-prefix ([#271](https://github.com/awslabs/jsii/issues/271)) ([03103f3](https://github.com/awslabs/jsii/commit/03103f3))
* require distinct argument and property names ([#272](https://github.com/awslabs/jsii/issues/272)) ([4d2f268](https://github.com/awslabs/jsii/commit/4d2f268)), closes [#268](https://github.com/awslabs/jsii/issues/268)




<a name="0.7.7"></a>
## [0.7.7](https://github.com/awslabs/jsii/compare/v0.7.6...v0.7.7) (2018-10-10)


### Bug Fixes

* **jsii:** better usage reporting of private types ([#247](https://github.com/awslabs/jsii/issues/247)) ([96ac5d6](https://github.com/awslabs/jsii/commit/96ac5d6))
* **jsii:** support  public autoproperties in private constructor ([#256](https://github.com/awslabs/jsii/issues/256)) ([181012e](https://github.com/awslabs/jsii/commit/181012e))
* **jsii:** use default jsx compiler options ([#260](https://github.com/awslabs/jsii/issues/260)) ([660ae79](https://github.com/awslabs/jsii/commit/660ae79)), closes [awslabs/aws-cdk#830](https://github.com/awslabs/aws-cdk/issues/830)




<a name="0.7.6"></a>
## [0.7.6](https://github.com/awslabs/jsii/compare/v0.7.5...v0.7.6) (2018-09-20)


### Bug Fixes

* **jsii:** Defaulted parameters were not rendered as optional ([#234](https://github.com/awslabs/jsii/issues/234)) ([578bf9c](https://github.com/awslabs/jsii/commit/578bf9c)), closes [#233](https://github.com/awslabs/jsii/issues/233)
* **jsii:** Don't skip emit on TS errors when in "watch" mode ([#236](https://github.com/awslabs/jsii/issues/236)) ([30d1491](https://github.com/awslabs/jsii/commit/30d1491)), closes [#235](https://github.com/awslabs/jsii/issues/235)
* **jsii:** Optional `any` represented as required ([#237](https://github.com/awslabs/jsii/issues/237)) ([91074f3](https://github.com/awslabs/jsii/commit/91074f3)), closes [#230](https://github.com/awslabs/jsii/issues/230)




<a name="0.7.5"></a>
## [0.7.5](https://github.com/awslabs/jsii/compare/v0.7.4...v0.7.5) (2018-09-13)


### Bug Fixes

* **java:** support abstract return types ([#224](https://github.com/awslabs/jsii/issues/224)) ([3257223](https://github.com/awslabs/jsii/commit/3257223)), closes [#220](https://github.com/awslabs/jsii/issues/220) [#223](https://github.com/awslabs/jsii/issues/223) [awslabs/aws-cdk#680](https://github.com/awslabs/aws-cdk/issues/680)




<a name="0.7.4"></a>
## [0.7.4](https://github.com/awslabs/jsii/compare/v0.7.3...v0.7.4) (2018-09-10)




**Note:** Version bump only for package jsii

<a name="0.7.3"></a>
## [0.7.3](https://github.com/awslabs/jsii/compare/v0.7.2...v0.7.3) (2018-09-06)


### Bug Fixes

* **jsii:** add readme and restore missing files in jsii tarball ([09f9fc9](https://github.com/awslabs/jsii/commit/09f9fc9))




<a name="0.7.2"></a>
## [0.7.2](https://github.com/awslabs/jsii/compare/v0.7.1...v0.7.2) (2018-09-06)


### Bug Fixes

* Missing types in JSII assembly, invalid Java code, confusing docs ([#208](https://github.com/awslabs/jsii/issues/208)) ([b37101f](https://github.com/awslabs/jsii/commit/b37101f)), closes [#175](https://github.com/awslabs/jsii/issues/175)


### Features

* **jsii:** Re-implemented jsii to support --watch and produce better error reporting ([#188](https://github.com/awslabs/jsii/issues/188)) ([76472be](https://github.com/awslabs/jsii/commit/76472be))




<a name="0.7.1"></a>
## [0.7.1](https://github.com/awslabs/jsii/compare/v0.7.0...v0.7.1) (2018-08-28)

### Features

* **jsii:** Add check against downgrading properties to readonly ([#201](https://github.com/awslabs/jsii/issues/201)) ([f60b0ac](https://github.com/awslabs/jsii/commit/f60b0ace014e8e96090ead808436b1ce0cb6b1e8))

<a name="0.7.0"></a>
# [0.7.0](https://github.com/awslabs/jsii/compare/v0.6.4...v0.7.0) (2018-08-21)


### Features

* **jsii:** Further normalize assembly outputs ([#177](https://github.com/awslabs/jsii/issues/177)) ([de3f062](https://github.com/awslabs/jsii/commit/de3f062)), closes [#60](https://github.com/awslabs/jsii/issues/60)




<a name="0.7.0"></a>
# [0.7.0](https://github.com/awslabs/jsii/compare/v0.6.4...v0.7.0) (2018-08-21)


### Features

* **jsii:** Further normalize assembly outputs ([#177](https://github.com/awslabs/jsii/issues/177)) ([de3f062](https://github.com/awslabs/jsii/commit/de3f062)), closes [#60](https://github.com/awslabs/jsii/issues/60)




<a name="0.6.4"></a>
## [0.6.4](https://github.com/awslabs/jsii/compare/v0.6.3...v0.6.4) (2018-08-08)




**Note:** Version bump only for package jsii

<a name="0.6.3"></a>
## [0.6.3](https://github.com/awslabs/jsii/compare/v0.6.2...v0.6.3) (2018-08-08)




**Note:** Version bump only for package jsii

<a name="0.6.2"></a>
## 0.6.2 (2018-08-07)




**Note:** Version bump only for package jsii
