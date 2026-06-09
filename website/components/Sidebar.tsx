import Link from 'next/link';
import { getModules, getDocumentsInModule } from '@/lib/markdown';
import styles from './Sidebar.module.css';
import SidebarNav from './SidebarNav';

export default function Sidebar({ locale = 'zh' }: { locale?: string }) {
  const prefix = locale === 'en' ? '/en/docs' : '/docs';
  
  const rawModules = getModules(locale);
  const modules = rawModules.map(mod => ({
    id: mod.id,
    title: mod.title,
    docs: getDocumentsInModule(mod.id, locale).map(doc => ({
      slug: doc.slug,
      title: doc.title
    }))
  }));

  return (
    <aside className={styles.sidebar}>
      <div className={styles.sidebarHeader}>
        <Link href={locale === 'en' ? '/en' : '/'} style={{color: 'inherit'}}>
          <h2>AI Landscape</h2>
        </Link>
      </div>
      <SidebarNav modules={modules} prefix={prefix} />
    </aside>
  );
}
