
import streamlit as st
from PIL import Image, ImageFilter


def download_file(image):
    with open(image, "rb") as file:
        st.download_button(
            label="Download",
            data=file,
            file_name=image,
            mime="image/png")


with st.expander("Open Camera"):
    camera_image = st.camera_input("Camera")

    option = st.selectbox("Select Option: ", ["Original", "Gray Scale", "Blur",
                                              "Contour", "Detail", "Edge Enhance",
                                              "More Edge Enhance", "Emboss", "Outline",
                                              "Sharpen", "Smooth", "More Smooth"])

    if camera_image:
        img = Image.open(camera_image)
        if option == "Original":
            st.image(img)
            img.save("original_img.png")
            download_file("original_img.png")

        if option == "Gray Scale":
            gray_image = img.convert("L")
            st.image(gray_image)
            gray_image.save("gray_img.png")
            download_file("gray_img.png")
        elif option == "Blur":
            blur_image = img.filter(ImageFilter.BLUR)
            st.image(blur_image)
            blur_image.save("blur_img.png")
            download_file("blur_img.png")
        elif option == "Contour":
            contour = img.filter(ImageFilter.CONTOUR)
            st.image(contour)
            contour.save("contour_img.png")
            download_file("contour_img.png")
        elif option == "Detail":
            detail = img.filter(ImageFilter.DETAIL)
            st.image(detail)
            detail.save("detail_img.png")
            download_file("detail_img.png")
        elif option == "Edge Enhance":
            edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)
            st.image(edge_enhance)
            edge_enhance.save("edge_enhanced.png")
            download_file("edge_enhanced.png")
        elif option == "ore Edge Enhance":
            more_edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            st.image(more_edge_enhance)
            more_edge_enhance.save("more_edge_enhanced.png")
            download_file("more_edge_enhanced.png")
        elif option == "Emboss":
            emboss = img.filter(ImageFilter.EMBOSS)
            st.image(emboss)
            emboss.save("emboss.png")
            download_file("emboss.png")
        elif option == "Outline":
            outline = img.filter(ImageFilter.FIND_EDGES)
            st.image(outline)
            outline.save("outline.png")
            download_file("outline.png")
        elif option == "Sharpen":
            sharpen = img.filter(ImageFilter.SHARPEN)
            st.image(sharpen)
            sharpen.save("sharpen.png")
            download_file("sharpen.png")
        elif option == "Smooth":
            smooth = img.filter(ImageFilter.SMOOTH)
            st.image(smooth)
            smooth.save("smooth.png")
            download_file("smooth.png")
        elif option == "More Smooth":
            more_smooth = img.filter(ImageFilter.SMOOTH_MORE)
            st.image(more_smooth)
            more_smooth.save("more_smooth.png")
            download_file("more_smooth.png")


