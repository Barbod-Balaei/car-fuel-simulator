
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# تعریف لیست خودروها و مشخصاتشان
cars = {
    "پراید": {"consumption": 7.5, "image": "pride.jpg"},
    "سمند": {"consumption": 8.5, "image": "samand.jpg"},
    "دنا": {"consumption": 9.2, "image": "dana.jpg"},
    "رانا": {"consumption": 8.2, "image": "dana.jpg"},
    "تارا": {"consumption": 7.8, "image": "tara.jpg"}
}

st.title("شبیه‌ساز هوشمند مصرف سوخت خودرو")

car_choice = st.selectbox("لطفاً خودرو را انتخاب کنید:", list(cars.keys()))
consumption = cars[car_choice]["consumption"]

st.markdown(f"**مصرف سوخت هر 100 کیلومتر:** {consumption} لیتر")

distance = st.number_input("مسافت سفر (کیلومتر):", min_value=0.0, value=100.0)
speed = st.number_input("سرعت متوسط (km/h):", min_value=1.0, value=80.0)
fuel_available = st.number_input("مقدار سوخت موجود در باک (لیتر):", min_value=0.0, value=20.0)
fuel_price = st.number_input("قیمت هر لیتر بنزین (تومان):", min_value=0.0, value=3000.0)

if st.button("محاسبه"):
    time = distance / speed
    fuel_needed = (distance * consumption) / 100
    cost = fuel_needed * fuel_price

    st.markdown(f"**زمان تقریبی سفر:** {time:.2f} ساعت")
    st.markdown(f"**مقدار سوخت مورد نیاز:** {fuel_needed:.2f} لیتر")
    st.markdown(f"**هزینه سفر:** {cost:,.0f} تومان")

    if fuel_available >= fuel_needed:
        st.success("سوخت موجود برای سفر کافی است.")
    else:
        st.warning("سوخت موجود برای این سفر کافی نیست!")

# نمایش تصویر خودرو
st.markdown("### تصویر خودرو انتخاب‌شده:")
try:
    image = Image.open(cars[car_choice]["image"])
    st.image(image, width=300)
except:
    st.info("عکس خودرو یافت نشد. لطفاً فایل تصویر را در مسیر مناسب قرار دهید.")

# رسم نمودار مقایسه‌ای
if st.button("نمایش نمودار مصرف سوخت خودروها"):
    names = list(cars.keys())
    values = [cars[name]["consumption"] for name in names]
    fig, ax = plt.subplots()
    ax.bar(names, values, color='skyblue')
    ax.set_ylabel("لیتر در 100 کیلومتر")
    ax.set_title("مقایسه مصرف سوخت خودروها")
    st.pyplot(fig)
