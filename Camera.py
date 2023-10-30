from io import BytesIO

import streamlit as st
from PIL import Image, ImageFilter


# buf = BytesIO()
with st.expander("Open Camera"):
    camera_image = st.camera_input("Camera")

    option = st.selectbox("Select Option: ", ["Original", "Gray Scale", "Blur",
                                              "Contour", "Detail", "Edge Enhance",
                                              "More Edge Enhance", "Emboss", "Outline",
                                              "Sharpen", "Smooth", "More Smooth"])

    if camera_image:
        img = Image.open(camera_image)
        if option == "Original":
            image = img

        if option == "Gray Scale":
            image = img.convert("L")

        elif option == "Blur":
            image = img.filter(ImageFilter.BLUR)

        elif option == "Contour":
            image = img.filter(ImageFilter.CONTOUR)

        elif option == "Detail":
            image = img.filter(ImageFilter.DETAIL)

        elif option == "Edge Enhance":
            image = img.filter(ImageFilter.EDGE_ENHANCE)

        elif option == "ore Edge Enhance":
            image = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

        elif option == "Emboss":
            image = img.filter(ImageFilter.EMBOSS)

        elif option == "Outline":
            image = img.filter(ImageFilter.FIND_EDGES)

        elif option == "Sharpen":
            image = img.filter(ImageFilter.SHARPEN)

        elif option == "Smooth":
            image = img.filter(ImageFilter.SMOOTH)

        elif option == "More Smooth":
            image = img.filter(ImageFilter.SMOOTH_MORE)

        st.image(image)
        image.save("image.png")
        with open("image.png", "rb") as file:
            st.download_button(label="Download", data=file, file_name="image.png",
                               mime="image/png")

        # st.image(image)
        # image.save(buf, format="JPEG")
        # file = buf.getvalue()
        # st.download_button(label="Download", data=file, file_name="image.jpeg",
        #                    mime="image/jpeg")
