import streamlit as st
import requests
import favicon

def get_favicon_url(site_url):
    try:
        icons = favicon.get(site_url)
        return icons[0].url if icons else "https://upload.wikimedia.org/wikipedia/commons/6/6b/Bitmap_Icon_Favicon.ico"
    except Exception:
        return "https://upload.wikimedia.org/wikipedia/commons/6/6b/Bitmap_Icon_Favicon.ico"

if "links" not in st.session_state:
    st.session_state.links = [
        {"name": "GitHub", "url": "https://github.com/"},
        {"name": "LinkedIn", "url": "https://linkedin.com/"},
        {"name": "YouTube", "url": "https://youtube.com/"},
        {"name": "Portfolio", "url": "https://yourportfolio.com/"},
        {"name": "Instagram", "url": "https://instagram.com/"},
    ]
if "menu_open" not in st.session_state:
    st.session_state.menu_open = [False]*len(st.session_state.links)

st.title("My Linktree")

st.write("Your links:")

for i, link in enumerate(st.session_state.links):
    favicon_url = get_favicon_url(link["url"])
    cols = st.columns([1, 8, 1])
    with cols[0]:
        st.image(favicon_url, width=32)
    with cols[1]:
        st.markdown(f"**[{link['name']}]({link['url']})**")
    with cols[2]:
        if st.button("⋮", key=f"dots_{i}"):
            st.session_state.menu_open[i] = not st.session_state.menu_open[i]
    if st.session_state.menu_open[i]:
        edit_col, remove_col = st.columns([1,1])
        with edit_col:
            if st.button("Edit", key=f"edit_{i}"):
                # Implement edit logic (prompt for new name/url and update)
                st.session_state.menu_open[i] = False
        with remove_col:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.links.pop(i)
                st.session_state.menu_open.pop(i)
                st.experimental_rerun()

st.markdown("---")
st.subheader("Add a new link")
new_name = st.text_input("Link name")
new_url = st.text_input("Link URL")
if st.button("Add Link"):
    st.session_state.links.append({"name": new_name, "url": new_url})
    st.session_state.menu_open.append(False)
    st.success(f"Added {new_name}")
