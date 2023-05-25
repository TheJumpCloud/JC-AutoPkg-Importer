## 0.2.0

Release Date: May 23, 2023

#### RELEASE NOTES

Bug-Fix release to address an issue where the importer would needlessly call the system insights API numerous times. This release introduces a new type of filter within `.jumpcloud` recipes. This filter is required if the importer is set to `update` or `auto` and should be set to the value of the software name as it's recorded within system insights. See the wiki pages for more information.

#### FEATURES

- New filter type to quickly discover which systems have 'x' software installed, this will decrease recipe runtime dramatically

## 0.1.3

Release Date: September 09, 2020

#### RELEASE NOTES

Initial release of JumpCloud AutoPkg importer

#### FEATURES

- Create dynamic JumpCloud commands from AutoPkg .pkg recipes
- JumpCloud commands can be scheduled with variables
- System Insights can be used to find systems with outdated AutoPkg recipe software.

#### IMPROVEMENTS

#### BUG FIXES

Recipes with spaces in the name are encoded correctly as URLs
