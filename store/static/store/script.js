/* ==========================================================================
   LUMORA BEAUTY STORE - INTERACTIVE JAVASCRIPT ENGINE
   ========================================================================== */

// --- 1. GLOBAL STATE DATA ---
let products = [
    {
        id: 1,
        name: "Korean Hydrating Serum",
        brand: "Beauty of Joseon",
        category: "SKINCARE",
        subCategory: "Serum",
        price: 1500,
        salePrice: 1200,
        image: "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?q=80&w=600",
        isBestSeller: true,
        isHotSale: true
    },
    {
        id: 2,
        name: "Japanese Repair Hair Mask",
        brand: "Shiseido Fino",
        category: "HAIRCARE",
        subCategory: "Hair Mask",
        price: 980,
        salePrice: null,
        image: "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?q=80&w=600",
        isBestSeller: true,
        isHotSale: false
    },
    {
        id: 3,
        name: "Velvet Matte Lipstick",
        brand: "LUMORA Beauty",
        category: "MAKEUP",
        subCategory: "Lips",
        price: 850,
        salePrice: 650,
        image: "https://images.unsplash.com/photo-1586495777744-4413f21062fa?q=80&w=600",
        isBestSeller: false,
        isHotSale: true
    },
    {
        id: 4,
        name: "Elegance Eau de Parfum",
        brand: "LUMORA Fragrance",
        category: "FRAGRANCE",
        subCategory: "For Her",
        price: 3500,
        salePrice: 2900,
        image: "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?q=80&w=600",
        isBestSeller: true,
        isHotSale: true
    }
];

let wishlist = [];
let activePromo = null;

// Shipping fees mapped by governorate
let shippingRates = {
    "Cairo": 70,
    "Giza": 70,
    "Alexandria": 80,
    "Dakahlia": 50,
    "Other": 100
};

// Promo Codes Store (Expiry date kept strictly internal)
let validPromoCodes = {
    "LUMORA10": { discountPercent: 10, expiry: "2026-12-31" },
    "SHAZA20": { discountPercent: 20, expiry: "2026-11-30" }
};

// --- 2. INITIALIZATION ON DOM LOAD ---
document.addEventListener("DOMContentLoaded", () => {
    renderProducts();
    renderBrands();
    updateWishlistUI();
});

// --- 3. PRODUCT RENDERING & FILTERING ---
function renderProducts() {
    const salesGrid = document.getElementById("sales-products-grid");
    const bestSellingGrid = document.getElementById("bestselling-products-grid");

    if (salesGrid) salesGrid.innerHTML = "";
    if (bestSellingGrid) bestSellingGrid.innerHTML = "";

    products.forEach(product => {
        const productHTML = createProductCardHTML(product);

        if (product.isHotSale && salesGrid) {
            salesGrid.innerHTML += productHTML;
        }
        if (product.isBestSeller && bestSellingGrid) {
            bestSellingGrid.innerHTML += productHTML;
        }
    });
}

function createProductCardHTML(product) {
    const currentPrice = product.salePrice ? product.salePrice : product.price;
    const oldPriceHTML = product.salePrice 
        ? `<span class="text-xs price-old line-through ml-2">${product.price.toLocaleString()} EGP</span>` 
        : '';
    const saleBadge = product.salePrice 
        ? `<span class="absolute top-2 left-2 z-10 sale-badge text-[10px] font-bold px-2 py-0.5 rounded uppercase">SALE</span>` 
        : '';

    return `
        <div class="product-card flex flex-col justify-between">
            <div class="relative aspect-square overflow-hidden bg-gray-50">
                ${saleBadge}
                <img src="${product.image}" alt="${product.name}" class="w-full h-full object-cover">
            </div>
            <div class="p-4 flex-1 flex flex-col justify-between">
                <div>
                    <span class="text-[10px] text-gray-500 uppercase font-semibold">${product.brand}</span>
                    <h3 class="font-medium text-sm mt-1 line-clamp-1">${product.name}</h3>
                </div>
                <div class="mt-4">
                    <div class="flex items-baseline">
                        <span class="price-current text-sm">${currentPrice.toLocaleString()} EGP</span>
                        ${oldPriceHTML}
                    </div>
                    <button onclick="addToWishlist(${product.id})" class="w-full mt-3 py-2.5 text-xs font-semibold uppercase flex items-center justify-center gap-2">
                        <i class="fa-solid fa-heart"></i> Add to Wishlist
                    </button>
                </div>
            </div>
        </div>
    `;
}

// Render dynamic list of unique brands
function renderBrands() {
    const container = document.getElementById("brands-container");
    if (!container) return;

    const uniqueBrands = [...new Set(products.map(p => p.brand))];
    container.innerHTML = uniqueBrands.map(brand => `
        <div class="border py-4 px-3 text-center rounded hover:shadow-sm transition cursor-pointer">
            <span class="font-serif font-bold text-xs uppercase tracking-wider">${brand}</span>
        </div>
    `).join('');
}

// --- 4. WISHLIST MANAGEMENT & CHECKOUT FLOW ---
function addToWishlist(productId) {
    const item = products.find(p => p.id === productId);
    if (!item) return;

    wishlist.push(item);
    updateWishlistUI();
    showToastNotification();
}

function removeFromWishlist(index) {
    wishlist.splice(index, 1);
    updateWishlistUI();
}

function updateWishlistUI() {
    const countBadge = document.getElementById("wishlist-count");
    const container = document.getElementById("wishlist-items-container");

    if (countBadge) countBadge.innerText = wishlist.length;

    if (!container) return;

    if (wishlist.length === 0) {
        container.innerHTML = `<p class="text-xs text-gray-500 text-center py-8">Your Wishlist is currently empty.</p>`;
    } else {
        container.innerHTML = wishlist.map((item, index) => {
            const price = item.salePrice ? item.salePrice : item.price;
            return `
                <div class="flex items-center justify-between gap-3 p-2 border-b border-gray-100">
                    <img src="${item.image}" class="w-12 h-12 object-cover rounded">
                    <div class="flex-1">
                        <h4 class="text-xs font-semibold line-clamp-1">${item.name}</h4>
                        <span class="text-xs font-bold">${price.toLocaleString()} EGP</span>
                    </div>
                    <button onclick="removeFromWishlist(${index})" class="text-gray-400 hover:text-red-500 p-1">
                        <i class="fa-solid fa-trash-can text-sm"></i>
                    </button>
                </div>
            `;
        }).join('');
    }

    calculateShipping();
}

// Toast Alert: Added successfully!
function showToastNotification() {
    const toast = document.getElementById("toast-notification");
    if (!toast) return;

    toast.classList.remove("hidden");
    setTimeout(() => {
        toast.classList.add("hidden");
    }, 2500);
}

// Toggle Wishlist Slide Drawer
function toggleWishlistDrawer() {
    const drawer = document.getElementById("wishlist-drawer");
    if (drawer) drawer.classList.toggle("hidden");
}

// --- 5. CALCULATIONS (SHIPPING, PROMO, FREE SHIPPING THRESHOLD) ---
function calculateShipping() {
    const govSelect = document.getElementById("governorate-select");
    const subtotal = wishlist.reduce((sum, item) => sum + (item.salePrice ? item.salePrice : item.price), 0);

    let shippingCost = 0;
    const selectedGov = govSelect ? govSelect.value : "";

    // Free shipping threshold over 4999 EGP rule
    if (subtotal >= 4999) {
        shippingCost = 0;
    } else if (selectedGov && shippingRates[selectedGov] !== undefined) {
        shippingCost = shippingRates[selectedGov];
    } else if (selectedGov) {
        shippingCost = shippingRates["Other"];
    }

    // Discount Calculation
    let discountAmount = 0;
    if (activePromo) {
        discountAmount = (subtotal * activePromo.discountPercent) / 100;
    }

    const total = subtotal + shippingCost - discountAmount;

    // Render Calculations in Cart Summary
    if (document.getElementById("summary-subtotal")) {
        document.getElementById("summary-subtotal").innerText = `${subtotal.toLocaleString()} EGP`;
        document.getElementById("summary-shipping").innerText = shippingCost === 0 && subtotal >= 4999 ? "FREE" : `${shippingCost} EGP`;
        document.getElementById("summary-total").innerText = `${Math.max(0, total).toLocaleString()} EGP`;

        const discountRow = document.getElementById("discount-row");
        const summaryDiscount = document.getElementById("summary-discount");
        if (discountRow && summaryDiscount) {
            if (discountAmount > 0) {
                discountRow.classList.remove("hidden");
                summaryDiscount.innerText = `-${discountAmount.toLocaleString()} EGP`;
            } else {
                discountRow.classList.add("hidden");
            }
        }
    }
}

// Apply Promo Code
function applyPromoCode() {
    const promoInput = document.getElementById("promocode-input");
    const promoMsg = document.getElementById("promo-message");
    if (!promoInput || !promoMsg) return;

    const code = promoInput.value.trim().toUpperCase();
    const foundCode = validPromoCodes[code];

    if (foundCode) {
        const today = new Date(). 