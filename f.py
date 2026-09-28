import streamlit as st

# ============================================================
# LA FILLE — QUICK FASHION DELIVERY
# Single-file Streamlit website
# ============================================================

st.set_page_config(
    page_title="La Fille | Fashion Delivered Fast",
    page_icon="🎀🧚",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #fffaf8;
    color: #3f3032;
}

/* Remove Streamlit top space */
.block-container {
    padding-top: 1rem;
    padding-bottom: 4rem;
    max-width: 1400px;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Main logo */
.logo {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    font-weight: 700;
    color: #b85c76;
    letter-spacing: 1px;
}

.logo-small {
    font-family: 'Playfair Display', serif;
    color: #b85c76;
    font-size: 27px;
    font-weight: 700;
}

/* Navigation */
.nav-text {
    text-align: center;
    font-size: 15px;
    color: #6d555a;
    padding-top: 12px;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #fff0f3, #fff8f1);
    border-radius: 30px;
    padding: 70px 65px;
    margin-top: 20px;
    margin-bottom: 45px;
    position: relative;
    overflow: hidden;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 65px;
    line-height: 1.05;
    color: #422f34;
    margin-bottom: 20px;
}

.hero h1 span {
    color: #c45f7d;
}

.hero p {
    font-size: 18px;
    color: #765f64;
    max-width: 560px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;
    background: #ffffff;
    color: #b34e6c;
    border-radius: 30px;
    padding: 10px 20px;
    font-weight: 600;
    margin-bottom: 20px;
}

.delivery-box {
    background: rgba(255,255,255,0.85);
    border: 1px solid #f4d9df;
    border-radius: 25px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(181, 92, 118, 0.08);
}

.delivery-number {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    color: #bf5975;
    font-weight: 700;
}

.delivery-text {
    color: #705b60;
}

/* Section headings */
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    color: #493438;
    margin-top: 25px;
}

.section-subtitle {
    color: #8b7378;
    margin-bottom: 25px;
}

/* Product cards */
.product-card {
    background: white;
    border: 1px solid #f3e0e3;
    border-radius: 22px;
    padding: 12px;
    margin-bottom: 18px;
    box-shadow: 0 7px 25px rgba(80, 40, 50, 0.05);
    transition: 0.3s;
}

.product-card:hover {
    box-shadow: 0 12px 30px rgba(180, 90, 115, 0.13);
    transform: translateY(-2px);
}

.product-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 17px;
}

.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 21px;
    color: #493438;
    margin-top: 12px;
}

.product-price {
    color: #b65471;
    font-weight: 700;
    font-size: 17px;
}

.old-price {
    color: #b9a4a8;
    text-decoration: line-through;
    font-size: 14px;
    margin-left: 7px;
}

.tag {
    display: inline-block;
    background: #fff0f3;
    color: #bd5874;
    padding: 5px 11px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
}

/* Buttons */
.stButton > button {
    border-radius: 25px !important;
    border: 1px solid #e9b9c5 !important;
    background: #fff !important;
    color: #a94e6b !important;
    font-weight: 600 !important;
    padding: 9px 20px !important;
    transition: 0.2s !important;
}

.stButton > button:hover {
    background: #fff0f3 !important;
    border-color: #c96884 !important;
}

.primary-btn .stButton > button {
    background: #c65f7b !important;
    color: white !important;
    border: none !important;
}

/* Info cards */
.info-card {
    background: #fff;
    border: 1px solid #f2dfe2;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    min-height: 150px;
}

.info-icon {
    font-size: 30px;
}

.info-title {
    font-weight: 700;
    color: #4b383c;
    margin-top: 8px;
}

.info-text {
    color: #8a7579;
    font-size: 14px;
}

/* Checkout */
.checkout-card {
    background: white;
    border: 1px solid #efdde0;
    border-radius: 25px;
    padding: 30px;
    box-shadow: 0 10px 35px rgba(100, 50, 60, 0.05);
}

.order-summary {
    background: #fff4f6;
    border-radius: 20px;
    padding: 25px;
}

.total {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    color: #b65471;
}

/* Success */
.success {
    background: linear-gradient(135deg, #fff0f3, #fff9f0);
    border: 1px solid #f0d4da;
    border-radius: 30px;
    text-align: center;
    padding: 70px 30px;
    margin-top: 40px;
}

.success-icon {
    font-size: 70px;
}

.success h1 {
    font-family: 'Playfair Display', serif;
    font-size: 45px;
    color: #493438;
}

.order-number {
    color: #b65471;
    font-weight: 700;
    font-size: 20px;
}

/* Footer */
.footer {
    margin-top: 70px;
    background: #fff0f3;
    border-radius: 25px;
    padding: 35px;
    text-align: center;
    color: #80686d;
}

.footer-logo {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    color: #b65471;
}

/* Mobile */
@media(max-width: 768px) {

    .hero {
        padding: 40px 25px;
    }

    .hero h1 {
        font-size: 42px;
    }

    .product-image {
        height: 230px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

if "cart" not in st.session_state:
    st.session_state.cart = []

if "order_placed" not in st.session_state:
    st.session_state.order_placed = False


# ============================================================
# PRODUCT DATA
# ============================================================

products = [
    {
        "id": 1,
        "name": "Rose Pink Midi Dress",
        "category": "Dresses",
        "price": 1499,
        "old": 1999,
        "size": "XS • S • M • L • XL",
        "image": "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=800",
        "description": "A soft rose-pink midi dress designed for effortless everyday elegance."
    },
    {
        "id": 2,
        "name": "Cream Satin Dress",
        "category": "Dresses",
        "price": 1899,
        "old": 2499,
        "size": "XS • S • M • L",
        "image": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=800",
        "description": "Elegant cream satin dress with a smooth finish and flattering silhouette."
    },
    {
        "id": 3,
        "name": "Blush Party Dress",
        "category": "Party Wear",
        "price": 2199,
        "old": 2999,
        "size": "XS • S • M • L • XL",
        "image": "https://images.unsplash.com/photo-1539008835657-9e8e9680c956?w=800",
        "description": "A beautiful blush-toned dress perfect for parties and special occasions."
    },
    {
        "id": 4,
        "name": "White Summer Dress",
        "category": "Summer",
        "price": 1299,
        "old": 1799,
        "size": "XS • S • M • L",
        "image": "https://images.unsplash.com/photo-1591369822096-ffd140ec948f?w=800",
        "description": "Lightweight white summer dress made for warm and sunny days."
    },
    {
        "id": 5,
        "name": "Pink Bow Dress",
        "category": "Trending",
        "price": 1699,
        "old": 2299,
        "size": "XS • S • M • L",
        "image": "https://images.unsplash.com/photo-1485968579580-b6d095142e6e?w=800",
        "description": "A feminine pink dress featuring a cute bow detail."
    },
    {
        "id": 6,
        "name": "Beige Mini Dress",
        "category": "Casual",
        "price": 1199,
        "old": 1599,
        "size": "XS • S • M • L • XL",
        "image": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=800",
        "description": "Minimal beige mini dress for a chic everyday look."
    },
    {
        "id": 7,
        "name": "Floral Pink Dress",
        "category": "Floral",
        "price": 1599,
        "old": 2099,
        "size": "XS • S • M • L",
        "image": "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=800",
        "description": "Pretty floral dress with a soft pink aesthetic."
    },
    {
        "id": 8,
        "name": "Elegant Black Dress",
        "category": "Evening",
        "price": 2299,
        "old": 2999,
        "size": "XS • S • M • L • XL",
        "image": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=800",
        "description": "A timeless black dress designed for evening occasions."
    }
]


# ============================================================
# NAVIGATION
# ============================================================

col1, col2, col3, col4, col5 = st.columns([2.5, 1, 1, 1, 1])

with col1:
    st.markdown('<div class="logo">La Fille 🎀</div>', unsafe_allow_html=True)

with col2:
    if st.button("Home"):
        st.session_state.page = "home"
        st.rerun()

with col3:
    if st.button("Shop"):
        st.session_state.page = "shop"
        st.rerun()

with col4:
    if st.button("Cart 🛍️"):
        st.session_state.page = "cart"
        st.rerun()

with col5:
    if st.button("Orders"):
        st.session_state.page = "checkout"
        st.rerun()

st.divider()


# ============================================================
# HOME PAGE
# ============================================================

def home_page():

    st.markdown("""
    <div class="hero">
        <div class="hero-badge">⚡ Fashion at your doorstep in 10–15 minutes</div>
        <h1>Style that arrives<br><span>before you change your mind.</span></h1>
        <p>
            Welcome to La Fille — your quick fashion destination.
            Discover beautiful dresses, choose your favourite look,
            place your order and get it delivered to your doorstep.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="info-card">
            <div class="info-icon">⚡</div>
            <div class="info-title">10–15 Min Delivery</div>
            <div class="info-text">Your fashion, delivered quickly.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
            <div class="info-icon">🎀</div>
            <div class="info-title">Trendy Styles</div>
            <div class="info-text">Fresh looks for every occasion.</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="info-card">
            <div class="info-icon">💗</div>
            <div class="info-title">Easy Shopping</div>
            <div class="info-text">Choose, order and relax.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">New Arrivals</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subtitle">Fresh styles picked especially for you.</div>',
        unsafe_allow_html=True
    )

    cols = st.columns(4)

    for i, product in enumerate(products[:4]):

        with cols[i]:

            st.markdown(
                f"""
                <div class="product-card">
                    <img class="product-image" src="{product['image']}">
                    <div class="tag">{product['category']}</div>
                    <div class="product-name">{product['name']}</div>
                    <div>
                        <span class="product-price">₹{product['price']}</span>
                        <span class="old-price">₹{product['old']}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button("View Dress", key=f"home_{product['id']}"):
                st.session_state.selected_product = product
                st.session_state.page = "product"
                st.rerun()

    st.markdown("""
    <div class="footer">
        <div class="footer-logo">La Fille 🎀</div>
        <p>Beautiful fashion. Fast delivery. Made for you.</p>
        <p>© 2026 La Fille — Quick Fashion Delivery</p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SHOP PAGE
# ============================================================

def shop_page():

    st.markdown('<div class="section-title">Shop La Fille</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-subtitle">Find your next favourite outfit.</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "🔎 Search dresses",
        placeholder="Search for a dress..."
    )

    categories = [
        "All",
        "Dresses",
        "Party Wear",
        "Summer",
        "Trending",
        "Casual",
        "Floral",
        "Evening"
    ]

    selected_category = st.selectbox(
        "Category",
        categories
    )

    filtered_products = products

    if search:
        filtered_products = [
            p for p in filtered_products
            if search.lower() in p["name"].lower()
        ]

    if selected_category != "All":
        filtered_products = [
            p for p in filtered_products
            if p["category"] == selected_category
        ]

    cols = st.columns(4)

    for i, product in enumerate(filtered_products):

        with cols[i % 4]:

            st.markdown(
                f"""
                <div class="product-card">
                    <img class="product-image" src="{product['image']}">
                    <div class="tag">{product['category']}</div>
                    <div class="product-name">{product['name']}</div>
                    <div>
                        <span class="product-price">₹{product['price']}</span>
                        <span class="old-price">₹{product['old']}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "View & Order",
                key=f"shop_{product['id']}"
            ):
                st.session_state.selected_product = product
                st.session_state.page = "product"
                st.rerun()


# ============================================================
# PRODUCT PAGE
# ============================================================

def product_page():

    product = st.session_state.selected_product

    if product is None:
        st.session_state.page = "shop"
        st.rerun()

    if st.button("← Back to Shop"):
        st.session_state.page = "shop"
        st.rerun()

    st.write("")

    left, right = st.columns([1.1, 1])

    with left:
        st.image(
            product["image"],
            use_container_width=True
        )

    with right:

        st.markdown(
            f'<div class="tag">{product["category"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="section-title">{product["name"]}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div>
                <span class="product-price" style="font-size:28px;">
                    ₹{product["price"]}
                </span>
                <span class="old-price">
                    ₹{product["old"]}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.write(product["description"])

        st.markdown("### Select Size")

        size = st.radio(
            "Size",
            ["XS", "S", "M", "L", "XL"],
            horizontal=True
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=10,
            value=1
        )

        st.markdown("""
        <div class="delivery-box">
            <div class="delivery-number">10–15 min</div>
            <div class="delivery-text">
                Estimated delivery to your location
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button("🛍️ Add to Cart", use_container_width=True):

            item = {
                "product": product,
                "size": size,
                "quantity": quantity
            }

            st.session_state.cart.append(item)

            st.success(
                f"{product['name']} added to your cart!"
            )

        if st.button(
            "⚡ Buy Now",
            use_container_width=True
        ):

            st.session_state.cart = [{
                "product": product,
                "size": size,
                "quantity": quantity
            }]

            st.session_state.page = "checkout"
            st.rerun()


# ============================================================
# CART PAGE
# ============================================================

def cart_page():

    st.markdown(
        '<div class="section-title">Your Shopping Bag 🛍️</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.cart:

        st.markdown("""
        <div class="success">
            <div class="success-icon">🛍️</div>
            <h1>Your bag is empty</h1>
            <p>Find something beautiful from our collection.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Start Shopping"):
            st.session_state.page = "shop"
            st.rerun()

        return

    total = 0

    for index, item in enumerate(st.session_state.cart):

        product = item["product"]
        quantity = item["quantity"]

        price = product["price"] * quantity
        total += price

        c1, c2, c3 = st.columns([1, 2, 1])

        with c1:
            st.image(
                product["image"],
                width=130
            )

        with c2:
            st.markdown(
                f"### {product['name']}"
            )

            st.write(
                f"Size: **{item['size']}**"
            )

            st.write(
                f"Quantity: **{quantity}**"
            )

        with c3:

            st.markdown(
                f"### ₹{price}"
            )

            if st.button(
                "Remove",
                key=f"remove_{index}"
            ):

                st.session_state.cart.pop(index)
                st.rerun()

        st.divider()

    st.markdown(
        f"""
        <div class="order-summary">
            <div>Total Items: {len(st.session_state.cart)}</div>
            <div class="total">Total: ₹{total}</div>
            <div>⚡ Estimated delivery: 10–15 minutes</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if st.button(
        "Continue to Checkout",
        use_container_width=True
    ):
        st.session_state.page = "checkout"
        st.rerun()


# ============================================================
# CHECKOUT PAGE
# ============================================================

def checkout_page():

    if not st.session_state.cart:

        st.warning("Your cart is empty.")

        if st.button("Go Shopping"):
            st.session_state.page = "shop"
            st.rerun()

        return

    st.markdown(
        '<div class="section-title">Order Details</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns([1.4, 0.8])

    with left:

        st.markdown(
            '<div class="checkout-card">',
            unsafe_allow_html=True
        )

        st.markdown("### 📍 Delivery Details")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your mobile number"
        )

        address = st.text_area(
            "Delivery Address",
            placeholder="House number, street, area..."
        )

        city = st.text_input(
            "City",
            placeholder="Enter your city"
        )

        pincode = st.text_input(
            "Pincode",
            placeholder="Enter pincode"
        )

        st.markdown("### 💳 Payment Method")

        payment = st.radio(
            "Choose payment",
            [
                "Cash on Delivery",
                "UPI",
                "Credit / Debit Card"
            ]
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    with right:

        total = 0

        for item in st.session_state.cart:
            total += (
                item["product"]["price"]
                * item["quantity"]
            )

        delivery_fee = 0

        st.markdown(
            f"""
            <div class="order-summary">

                <h3>Order Summary</h3>

                <p>Items: {len(st.session_state.cart)}</p>

                <p>Subtotal: ₹{total}</p>

                <p>Delivery: <b>FREE</b></p>

                <hr>

                <div class="total">
                    ₹{total}
                </div>

                <p>⚡ Delivery in 10–15 minutes</p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "💗 Place Order",
            use_container_width=True
        ):

            if not name or not phone or not address:

                st.error(
                    "Please fill in your name, phone number and address."
                )

            else:

                st.session_state.order_placed = True
                st.session_state.page = "success"
                st.rerun()


# ============================================================
# SUCCESS PAGE
# ============================================================

def success_page():

    st.markdown("""
    <div class="success">

        <div class="success-icon">🎀</div>

        <h1>Order Confirmed!</h1>

        <p>
            Thank you for shopping with La Fille.
        </p>

        <p class="order-number">
            Order #LF2026
        </p>

        <br>

        <h2>⚡ Your order is on its way</h2>

        <p>
            Estimated delivery time
        </p>

        <div class="delivery-number">
            10–15 MIN
        </div>

        <p>
            Please keep your phone available for the delivery partner.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "Continue Shopping",
            use_container_width=True
        ):

            st.session_state.cart = []
            st.session_state.order_placed = False
            st.session_state.page = "shop"
            st.rerun()

    with c2:

        if st.button(
            "Back to Home",
            use_container_width=True
        ):

            st.session_state.cart = []
            st.session_state.order_placed = False
            st.session_state.page = "home"
            st.rerun()


# ============================================================
# PAGE ROUTER
# ============================================================

if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "shop":
    shop_page()

elif st.session_state.page == "product":
    product_page()

elif st.session_state.page == "cart":
    cart_page()

elif st.session_state.page == "checkout":
    checkout_page()

elif st.session_state.page == "success":
    success_page()
