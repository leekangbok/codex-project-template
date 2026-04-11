# 🧰 AI Skills Catalog

이 디렉토리는 AI 에이전트가 고품질의 작업을 수행할 수 있도록 돕는 표준화된 워크플로우와 가이드라인(Skills)을 담고 있습니다. 각 스킬은 특정 상황에서 자동으로 트리거되거나 에이전트가 스스로 참조하여 최상의 결과를 낼 수 있도록 설계되었습니다.

---

## 🌐 시스템 워크플로우 (System Workflows)

기본적으로 제공되는 강력한 AI 도구들입니다.

| 스킬명 | 트리거 및 용도 |
| :--- | :--- |
| **`algorithmic-art`** | p5.js를 이용한 알고리즘 예술 생성 (Flow fields, particle systems 등) |
| **`brand-guidelines`** | 문서나 디자인에 Anthropic 브랜드 테마(Poppins, Lora 폰트 및 컬러) 적용 |
| **`canvas-design`** | 포스터, 아트워크 등 시각적 디자인이 필요한 정적 이미지(.png, .pdf) 작업 |
| **`claude-api`** | Claude API 또는 Anthropic SDK를 사용한 애플리케이션 개발 |
| **`doc-coauthoring`** | 기술 명세서, 제안서 등 구조화된 문서 공동 작성 및 리더 테스트 |
| **`docx`** | Word 문서 생성, 편집, 데이터 추출 및 포맷팅 |
| **`frontend-design`** | 고품질 프론트엔드 인터페이스(React, Tailwind) 및 웹 UI 개선 |
| **`internal-comms`** | 주간 보고서, 리더십 업데이트, 장애 보고서 등 사내 커뮤니케이션 작성 |
| **`karpathy-guidelines`** | 복잡성 감소 및 수술적 코드 변경을 위한 Karpathy식 코딩 원칙 |
| **`mcp-builder`** | 외부 서비스 연동을 위한 MCP(Model Context Protocol) 서버 개발 |
| **`pdf`** | PDF 텍스트 추출, 병합, 분할, OCR 및 신규 생성 |
| **`pptx`** | 프리젠테이션 슬라이드 생성, 분석 및 디자인 개선 |
| **`skill-creator`** | 새로운 AI 스킬 생성, 평가 및 설명문 최적화 |
| **`slack-gif-creator`** | Slack 환경에 최적화된 애니메이션 GIF 생성 |
| **`theme-factory`** | 문서나 슬라이드에 적용할 10가지 프리셋 테마 제공 |
| **`web-artifacts-builder`** | React/Tailwind 기반의 복잡한 HTML 아티팩트 빌드 |
| **`webapp-testing`** | Playwright를 이용한 로컬 웹 애플리케이션 자동화 테스트 |
| **`xlsx`** | 스프레드시트 데이터 분석, 수식 최적화 및 전문적 포맷팅 |

---

## 🛠️ 소프트웨어 개발 커스텀 스킬 (Custom Software Dev Skills)

실무 개발 환경에서 일관된 품질을 유지하기 위한 전용 가이드들입니다.

| 스킬명 | 용도 |
| :--- | :--- |
| **`refactoring-expert`** | 코드 가독성 및 유지보수성 향상을 위한 전문 리팩토링 가이드 |
| **`code-review-checklist`** | 보안, 성능, 로직 에러를 방지하기 위한 종합 코드 리뷰 체크리스트 |
| **`database-design`** | 효율적인 스키마 설계, 인덱싱 및 정규화 전략 |
| **`git-conventions`** | 브랜치 전략 및 Conventional Commits 메시지 규격 준수 |
| **`security-audit`** | 주입 공격, XSS 등 보안 취약점 점검 방법론 |
| **`error-handling-logging`** | 견고한 에러 관리 및 디버깅을 위한 구조화된 로깅 원칙 |
| **`production-ready-check`** | 운영 배포 전 최종 검증(신뢰성, 보안, 옵서버빌리티) 체크리스트 |

---

## 📖 사용 방법

1.  **에이전트**: 작업을 시작하기 전 `skills/` 내의 관련 문서를 먼저 읽고 워크플로우를 숙지하세요.
2.  **사용자**: 특정 스킬 사용을 명시적으로 요청하거나(`Karpathy 가이드라인에 맞춰 수정해줘`), 에이전트가 상황에 맞는 스킬을 제안하도록 할 수 있습니다.
