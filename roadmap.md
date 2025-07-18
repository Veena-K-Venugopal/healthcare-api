# 🛣️ Project Roadmap – Healthcare API Enhancer

This roadmap tracks the development phases and major milestones of the `healthcare-api` project.

---

## ✅ Phase 1 – Modular Structure + Mock Prediction

- [x] Refactored project into `app/` layout with `routes`, `services`, and `utils`
- [x] Created `/predict` endpoint using FastAPI and APIRouter
- [x] Built mock `predict()` logic and `enhancer.py` to enrich results
- [x] Swagger UI functional with live docs
- [x] Deployed working version to Render
- [x] README updated to reflect accurate live features

🟢 **Status**: Completed  
📅 Completed: July 2025

---

## 🔄 Phase 2 – Real ML Model Integration

- [ ] Choose public dataset (e.g., diabetes or heart disease)
- [ ] Train ML model using scikit-learn (logistic regression, etc.)
- [ ] Save model as `model.pkl` in `models/` directory
- [ ] Create `model_service.py` to load and use model for prediction
- [ ] Replace mock logic in `/predict` route with real output
- [ ] Validate input schema and improve error handling
- [ ] Add unit test(s) for `/predict`
- [ ] Update README with model details

🟡 **Status**: In Progress

---

## 🧠 Phase 3 – Input Validation, Caching, Logging

- [ ] Add custom input validation (Pydantic + manual checks)
- [ ] Implement basic caching (optional: Redis or in-memory)
- [ ] Add request/response logging (timestamp, endpoint, etc.)
- [ ] Improve error responses and fallback handling

🟠 **Status**: Planned

---

## 🌟 Future Enhancements (Post-Core Phases)

- [ ] Add `/upload` route for batch predictions
- [ ] Add database (PostgreSQL or SQLite) for persistent patient records
- [ ] Build frontend dashboard (React, Next.js, or Streamlit)
- [ ] Add user authentication
- [ ] Containerize with Docker and deploy full-stack version

🔮 **Status**: Wishlist
