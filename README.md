# badges

Generate and cache informational badges

Install with `pip install .`

### Conda

Monthly conda download badges can be generated with:
```bash
❯ generate-conda-badges -p bokeh -p panel --logo anaconda
{
  "bokeh": "https://img.shields.io/badge/conda-598k%2Fmonth-goldenrod?style=for-the-badge&logo=anaconda",
  "panel": "https://img.shields.io/badge/conda-158k%2Fmonth-goldenrod?style=for-the-badge&logo=anaconda"
}
```

Several options are configurable:
```
Usage: generate-conda-badges [OPTIONS]

  Generate shields.io badge URLs with monthly conda package download numbers

Options:
  -p, --package TEXT              Conda package name to generate a badge for
                                  [default: bokeh]
  -m, --month [%Y-%m]             A month to collect data for expressed as
                                  YYYY-MM
  -c, --color TEXT                Highlight color for the badge  [default:
                                  goldenrod]
  -s, --style [plastic|flat|flat-square|for-the-badge|social]
                                  Style type for shields.io badge  [default:
                                  for-the-badge]
  -l, --label TEXT                Label for the badge. If '__name__' is
                                  passed, use package names for each label
                                  [default: conda]
  --logo TEXT                     A shields.io named logo for the badge
  --help                          Show this message and exit.
```
