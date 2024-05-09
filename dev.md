# Development mode
## Test local dev version
```sh
pdm dev-backend
pdm dev
```

## Test local built version
```sh
pdm start
```


# Release version
- Build backend
```shell
cd audio_recorder_streamlit/frontend
npm run build
```

- Change `_RELEASE` to `True` in `audio_recorder_streamlit/__init__.py`.
- Update the package version.
- Update the changelog.
- Remove presious distributions `rm -rf dist build *.egg-info`
- Build package distribution `pdm build`
- Test deployment with `pdm deploy-test`
- Deploy package with `pdm deploy`.
