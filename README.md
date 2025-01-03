# S4

Simple Screenshot Storage Service. Need anymore context? Python. That's all you get. Oh, you want more? **TOO BAD.**

## Architecture

```
└── app
    ├── aws
    ├── http
    ├── ss
    │   └── ocr
    └── util
```

`app/aws - AWS S3 integration.
`app/http` - Base HTTP server features.
`app/ss` - Screenshot handling and validation features.
`app/ss/ocr` - Raw screenshot export sorter with OCR.
`app/util` - Helper utilities.

## Milestones/feature ToDo list

- [ ] Figure out a CI/CD pipeline (SSH into TransEdenV3, push-n-pull code and run it).
- [ ] Write a CLI interface for the HTTP server.
- [ ] Display screenshot data in the right order.
- [ ] Validate screenshot data (feature/function).
- [ ] MD5 check screenshots (feature/function).
- [ ] Compress, send, receive and transform screenshots into the proper format from TransEdenV4 to TransEdenV3 ~~baby's first ETL~~.
- [ ] Upload to AWS S3 Glacier securely.
- [ ] I-yAM! batshit insane security integration.